// get a tags
const aTags = document.querySelectorAll('a[data-original-title="Download source file"]');

// 
aTags.forEach(aTag => {
  aTag.setAttribute('download', '');
});