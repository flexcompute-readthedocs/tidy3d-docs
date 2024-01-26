import json
import os
import pathlib
import shutil
import re
import yaml  # pip install PyYAML


def get_file_directory():
    return pathlib.Path(__file__)


def extract_content_between_dashed(content):
    pattern = re.compile(r'---\n(.*?)\n---', re.DOTALL)
    match = pattern.search(content)
    if match:
        yml_content = yaml.safe_load(match.group(1).strip())
        # You can convert it to JSON format or other format if you needed
    else:
        yml_content = None
    return yml_content

def remove_jekyll_constructions(content):
    # Regex pattern to match constructions like {: ... }
    pattern = r'\{: .*?\}'
    # Replace matched patterns with an empty string
    cleaned_content = re.sub(pattern, '', content)

    return cleaned_content


def remove_nbsp_instances(content):
    # Replace HTML &nbsp; entity
    content = re.sub(r'&nbsp;', ' ', content)

    # Replace Unicode non-breaking space character
    content = content.replace(u'\xa0', ' ')

    return content

def preprocess_markdown_file(source_file, dest_file):
    with open(source_file, 'r') as f:
        content = f.read()

    metadata = extract_content_between_dashed(content)
    if metadata:
        title = metadata.get('title', 'Untitled')
        date = metadata.get('date', 'Unknown Date')
        category = metadata.get('category', 'Uncategorized')
        version = metadata.get('version')  # Optional version number

    # Remove the front matter (between the '---' lines)
    content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)

    # Construct the Markdown table, including the version if it exists
    table_content = f'| Date       | Category    |'
    table_separator = f'|------------|-------------|'
    table_data = f'| {date} | {category} |'

    if version is not None:
        table_content += ' Version |'
        table_separator += '---------|'
        table_data += f' {version} |'

    new_header = f'# {title}\n\n{table_content}\n{table_separator}\n{table_data}\n\n'
    content = new_header + content

    # Replace specific HTML constructions with Markdown code blocks
    pattern = r'(<div>)?<div markdown class="code-snippet">.*?{% highlight python %}(.*?)\{% endhighlight %}.*?(</div>)?</div>'
    replacement = r'\n\n```python\2```\n\n'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    content = remove_jekyll_constructions(content)
    content = remove_nbsp_instances(content)

    # Remove specific leftover HTML tags
    tags_to_remove = ['<p>', '</p>', '<div>', '</div>', "<span>", "</span>"]
    for tag in tags_to_remove:
        content = content.replace(tag, '')

    with open(dest_file, 'w') as f:
        f.write(content)


def copy_and_process_file(src, dst, *, follow_symlinks=True):
    # Check if it's a markdown file
    if src.endswith('.md'):
        preprocess_markdown_file(src, dst)
    else:
        # Simply copy the file
        shutil.copy2(src, dst, follow_symlinks=follow_symlinks)


def copy_and_process_directory(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for item in os.listdir(source_directory):
        source_item = os.path.join(source_directory, item)
        destination_item = os.path.join(destination_directory, item)

        if os.path.isdir(source_item):
            if os.path.exists(destination_item):
                # If the destination directory exists, copy each item in it separately
                copy_and_process_directory(source_item, destination_item)
            else:
                # If the destination directory doesn't exist, use copytree
                shutil.copytree(source_item, destination_item, copy_function=copy_and_process_file)
        else:
            # Process and copy files (overwrite if exists)
            copy_and_process_file(source_item, destination_item)


def create_rst_categories_from_json(json_file, output_dir):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for category in data:
        category_id = category['id']
        category_title = category['category']
        faqs = category['faqs']

        rst_content = f"{category_title}\n"
        rst_content += "=" * len(category_title) + "\n\n"
        rst_content += ".. toctree::\n"
        rst_content += "   :maxdepth: 2\n\n"

        for faq in faqs:
            # Assuming the path in the JSON is the relative path to the RST files
            # Remove the '_faqs/' prefix and '.md' suffix, replace with correct format if needed
            faq_relative_path = faq.replace('_faqs/', 'faq/').replace('.md', '')
            rst_content += f"   {faq_relative_path}\n"

        rst_file_path = os.path.join(output_dir, f"{category_id}.rst")
        with open(rst_file_path, 'w') as rst_file:
            rst_file.write(rst_content)


def create_toctree_for_rst_files(source_directory, output_file, title="FAQ |:mag_right:|"):
    """
    Creates a main .rst file with a toctree that references all .rst files in the specified directory.

    Args:
    source_directory (str): Directory containing .rst files.
    output_file (str): Path of the output file to write the toctree.
    title (str): Title for the main documentation file.
    """
    with open(output_file, 'w') as outfile:
        outfile.write(f"{title}\n")
        outfile.write("=" * len(title) + "\n\n")
        outfile.write(".. toctree::\n")
        outfile.write("   :maxdepth: 2\n\n")  # Adjust maxdepth as needed

        # Loop through all files in the directory
        for filename in sorted(os.listdir(source_directory)):
            if filename.endswith('.rst') and filename != os.path.basename(output_file):
                # Write the filename (without extension) to the toctree
                outfile.write(f"   {os.path.splitext(filename)[0]}\n")


if __name__ == "__main__":
    faq_directory = get_file_directory().parent.parent
    raw_faq_directory = faq_directory / "_faqs"
    json_file_path = faq_directory / "faq_categories.json"  # Update with the path to your JSON file
    output_directory = faq_directory / "docs"  # Update with your desired output directory
    processed_faq_directory = output_directory / "faq"
    compiled_index_file = output_directory / "index.rst"  # Update with your desired output file
    copy_and_process_directory(raw_faq_directory, processed_faq_directory)
    create_rst_categories_from_json(json_file_path, output_directory)
    create_toctree_for_rst_files(output_directory, compiled_index_file)
