/* Simple progressive enhancement for SignalScan site */
document.addEventListener('DOMContentLoaded', function () {
  // Replace links with fallback if placeholders are not configured
  const placeholderPattern = /\{\{.+?\}\}/;
  document.querySelectorAll('a').forEach(function (link) {
    if (placeholderPattern.test(link.getAttribute('href'))) {
      // Provide a generic fallback – send to mailto or anchor
      link.setAttribute('href', 'mailto:contact@example.com');
      link.addEventListener('click', function (e) {
        alert('Form link is not yet configured. Please email us at contact@example.com');
      });
    }
  });
});