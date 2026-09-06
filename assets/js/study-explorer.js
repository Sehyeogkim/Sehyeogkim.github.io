(() => {
  'use strict';

  const explorer = document.querySelector('details[data-study-explorer]');
  if (!explorer) return;

  const folders = Array.from(explorer.querySelectorAll('details[data-tree-key]'));
  const desktop = window.matchMedia('(min-width: 1000px)');
  const section = (explorer.dataset.explorerSection || 'Study').toLowerCase();
  const storageKey = `personal-blog-${section}-tree`;
  const panelStorageKey = `personal-blog-${section}-explorer-open`;
  const states = Object.create(null);

  try {
    const saved = JSON.parse(window.localStorage.getItem(storageKey) || '{}');
    if (saved && typeof saved === 'object' && !Array.isArray(saved)) {
      Object.entries(saved).forEach(([key, value]) => {
        if (typeof value === 'boolean') states[key] = value;
      });
    }
  } catch (_) {
    // Native folders remain usable without browser storage.
  }

  folders.forEach((folder) => {
    const key = folder.dataset.treeKey;
    if (Object.prototype.hasOwnProperty.call(states, key)) {
      folder.open = states[key];
    }
    if (folder.dataset.currentBranch === 'true') folder.open = true;
  });

  const save = () => {
    folders.forEach((folder) => {
      states[folder.dataset.treeKey] = folder.open;
    });
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(states));
    } catch (_) {
      // Folder navigation does not require persistent storage.
    }
  };

  folders.forEach((folder) => folder.addEventListener('toggle', save));

  explorer.querySelectorAll('[data-tree-collapse]').forEach((button) => {
    button.addEventListener('click', (event) => {
      event.preventDefault();
      folders.forEach((folder) => { folder.open = false; });
      save();
    });
  });

  let panelOpen = desktop.matches;
  try {
    const saved = window.localStorage.getItem(panelStorageKey);
    if (saved === 'true' || saved === 'false') panelOpen = saved === 'true';
  } catch (_) {
    // Use the initial viewport default when a saved preference is unavailable.
  }
  explorer.open = panelOpen;
  explorer.addEventListener('toggle', (event) => {
    if (event.target !== explorer) return;
    try {
      window.localStorage.setItem(panelStorageKey, String(explorer.open));
    } catch (_) {
      // Native folding remains available without persistent storage.
    }
  });

  // Reveal the current file inside the desktop panel without scrolling the article.
  requestAnimationFrame(() => {
    const current = explorer.querySelector('.explorer-file[aria-current="page"]');
    const panel = document.getElementById('panel-wrapper');
    if (!desktop.matches || !explorer.open || !current || !panel) return;
    const row = current.getBoundingClientRect();
    const bounds = panel.getBoundingClientRect();
    if (row.bottom > bounds.bottom || row.top < bounds.top) {
      panel.scrollTop += row.top - bounds.top - panel.clientHeight / 2 + row.height / 2;
    }
  });
})();
