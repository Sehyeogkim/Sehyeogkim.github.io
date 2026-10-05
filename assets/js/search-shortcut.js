(() => {
  'use strict';

  // Press "/" anywhere outside a text field to jump to search.
  document.addEventListener('keydown', (event) => {
    if (event.key !== '/' || event.metaKey || event.ctrlKey || event.altKey) return;
    const target = event.target;
    if (target instanceof HTMLElement && (target.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(target.tagName))) return;
    const input = document.getElementById('search-input');
    if (!input || input.offsetParent === null) return;
    event.preventDefault();
    input.focus();
  });
})();
