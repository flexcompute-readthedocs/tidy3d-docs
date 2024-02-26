import os
import re
import glob
import configparser
import yaml
import json
import shutil
from datetime import datetime
from algoliasearch.search_client import SearchClient
from slugify import slugify


class Configure:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config = configparser.ConfigParser()
    config_path = os.path.abspath(os.path.join(script_directory, './config.ini'))
    config.read(config_path)
    algolia_config = {}
    for section in config.sections():
        if section == 'Algolia':
            for key, value in config.items(section):
                algolia_config[key] = value

    # 获取配置项
    
    directory = config.get('General', 'compile_directory')
    compile_directory = os.path.abspath(os.path.join(
        script_directory, directory))
    compile_img_directory = os.path.abspath(os.path.join(
        script_directory, config.get('General', 'compile_img_directory')))
    faq_categories_path = os.path.abspath(os.path.join(
        script_directory, config.get('General', 'faq_categories')))
    faq_temp_directory = os.path.abspath(os.path.join(
        script_directory, config.get('General', 'faqs_temp_directory')))
    faq_temp_categories_path = os.path.abspath(os.path.join(script_directory, config.get('General', 'faq_temp_categories')))
    target_img_path = config.get('General', 'target_img_path')


class Sync:

    client = None

    def __init__(self) -> None:
        self.client = SearchClient.create(
            Configure.algolia_config['app_id'], Configure.algolia_config['api_key'])

    def upload_faq_suggestion(self, objects):
        if not self.client:
            return

        index = self.client.init_index(Configure.algolia_config['index_name'])
        index.replace_all_objects(objects, {
            'safe': True
        })


class Convert:
    md_files = []
    faq_categories = None
    titles = []

    def __init__(self) -> None:
        self.load_faq_categorie()
        self.files_to_compile()
        pass
    pass

    def load_faq_categorie(self):
        with open(Configure.faq_categories_path, 'r', encoding='utf-8') as json_file:
            self.faq_categories = json.load(json_file)
            # for item in self.faq_categories:
            #     item['id'] = slugify(item['id'])

    def get_relative_path(self, file_a, file_b):
        abs_path_a = os.path.abspath(file_a)
        abs_path_b = os.path.abspath(file_b)
        dir_a = os.path.dirname(abs_path_a)
        relative_path = os.path.relpath(abs_path_b, dir_a)
        return relative_path

    def is_file_exists(self, file_path):
        return os.path.exists(file_path) and os.path.isfile(file_path)

    def copy_faq_to_target(self, faq_path):
        if not os.path.exists(Configure.faq_temp_directory):
            os.makedirs(Configure.faq_temp_directory)

        shutil.copy2(faq_path, Configure.faq_temp_directory)

    def replacement_callback(self, img_path):
        img_name = os.path.basename(img_path)
        absolute_path = os.path.abspath(os.path.join(
            Configure.compile_img_directory, img_name))
        if self.is_file_exists(absolute_path):
            return os.path.join(Configure.target_img_path, img_name)
        else:
            return img_path

    def compile_images(self, content):
        # .md format
        image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

        def replace_image_md(match):
            # 如果有新图片链接，则使用新链接，否则保持原样
            old_image_path = match.group(1)
            new_image_url = self.replacement_callback(old_image_path)
            return match.group(0).replace(old_image_path, new_image_url)

        updated_content = image_pattern.sub(replace_image_md, content)
        # .html format
        html_image_pattern = re.compile(
            r'<img\s+.*?src=["\'](.*?)["\'].*?>', re.DOTALL)

        def replace_image(match):
            # 如果有新图片链接，则使用新链接，否则保持原样
            new_image_url = self.replacement_callback(match.group(1))
            # 替换src属性
            return match.group(0).replace(match.group(1), new_image_url)

        updated_content = html_image_pattern.sub(
            replace_image, updated_content)
        return updated_content

    def compile_faq(self, content):
        dict = self.extract_content_between_dashed(content)
        front_matter = dict['front_matter']
        excerpt_content = dict['content']
        front_matter['id'] = slugify(front_matter.get('title'))
        new_content = self.compile_images(excerpt_content)
        return {
            "front_matter": front_matter,
            "content": new_content
        }

    def write_new_faq(self, new_faq, path):
        md_file_name = os.path.basename(path)
        new_md_file = os.path.join(Configure.faq_temp_directory, md_file_name)
        front_matter = new_faq['front_matter']
        content = new_faq['content']
        yml_str = '---\n' + yaml.dump(front_matter) + '---\n'
        with open(new_md_file, 'w', encoding='utf-8') as file:
            file.write(yml_str + str(content))

    def compare_faq_category(self, faq_path, category):
        absolute_path = os.path.abspath(os.path.join(
            Configure.script_directory, '../', faq_path))
        if not self.is_file_exists(absolute_path):
            return {
                'exists': False
            }
        faq_category = ''
        faq_content = None
        enabled = False
        with open(absolute_path, 'r', encoding='utf-8') as file:
            faq_content = file.read()
            dict = self.extract_content_between_dashed(faq_content)
            front_matter = dict['front_matter']
            faq_category = front_matter.get('category')
            enabled = front_matter.get('enabled')
        file.close()
        return {
            'exists': category == faq_category and enabled,
            'content': faq_content
        }

    def faq_categorize(self, json_data, path):
        if not json_data.get("enabled"):
            return
        category = json_data.get('category')
        is_find = False
        relative_path = self.get_relative_path(
            Configure.faq_categories_path, path)
        # push new faq to the list
        for item in self.faq_categories:
            if item['category'] == category:
                is_find = True
                if 'faqs' not in item:
                    item['faqs'] = []
                if relative_path not in item['faqs']:
                    item['faqs'].append(relative_path)
        if not is_find:
            new_item = {}
            new_item['category'] = category
            new_item['id'] = slugify(category)
            new_item['faqs'] = [relative_path]
            self.faq_categories.append(new_item)

    def filter_faqs(self):
        # remove faqs that do not belong to the current category
        for item in self.faq_categories:
            if 'faqs' not in item:
                continue
            for faq_path in item['faqs']:
                dict = self.compare_faq_category(faq_path, item['category'])
                if dict['exists']:
                    new_faq = self.compile_faq(dict['content'])
                    self.write_new_faq(new_faq, faq_path)
                else:
                    item['faqs'].remove(faq_path)

    def files_to_compile(self):
        directory = Configure.compile_directory
        self.md_files = glob.glob(os.path.join(
            directory, '**', '*.md'), recursive=True)

    def formate_date(self, yml_content):
        if 'date' in yml_content:
            datetime_value = yml_content['date']
            if isinstance(datetime_value, datetime):
                formatted_date = datetime_value.strftime("%Y-%m-%d %H:%M:%S")
                yml_content['date'] = formatted_date
        return yml_content

    def extract_content_between_dashed(self, content):
        pattern = re.compile(r'---\n(.*?)\n---', re.DOTALL)
        match = pattern.search(content)
        if match:
            yml_content = yaml.safe_load(match.group(1).strip())
            return {
                "front_matter": json.loads(json.dumps(self.formate_date(yml_content))),
                "content": content[match.end():]
            }
        else:
            return None

    def generator_suggestion_title(self, json_data):
        if (json_data.get('enabled')):
            suggestion_info = {}
            suggestion_info['objectID'] = json_data.get('title')
            suggestion_info['query'] = json_data.get('title')
            suggestion_info['category'] = "FAQ"
            suggestion_info['popularity'] = 1
            self.titles.append(suggestion_info)

    def compile_md_files(self):
        for file_path in self.md_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                dict = self.extract_content_between_dashed(content)
                front_matter = dict['front_matter']
                if front_matter.get('enabled'):
                    self.generator_suggestion_title(front_matter)
                    self.faq_categorize(front_matter, file_path)
            file.close()

    def clear_temp_folder(self):
        if os.path.exists(Configure.faq_temp_directory):
            shutil.rmtree(Configure.faq_temp_directory)
        os.mkdir(Configure.faq_temp_directory)

    def generate_category_yml(self):
        toc_yml = yaml.dump(self.faq_categories)

        with open(Configure.faq_temp_categories_path, 'w') as f:
            f.write(toc_yml)
        f.close()
        pass

if __name__ == '__main__':
    convert = Convert()
    convert.compile_md_files()
    if len(convert.titles) > 0:
        sync = Sync()
        sync.upload_faq_suggestion(convert.titles)
    convert.clear_temp_folder()
    convert.filter_faqs()
    if convert.faq_categories:
        convert.generate_category_yml()
