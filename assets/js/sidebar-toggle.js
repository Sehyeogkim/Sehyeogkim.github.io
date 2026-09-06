(() => {
  'use strict';

  const sidebar = document.getElementById('sidebar');
  if (!sidebar || document.getElementById('sidebar-collapse-toggle')) return;

  const desktop = window.matchMedia('(min-width: 850px)');
  const storageKey = 'personal-blog-sidebar-collapsed';
  let collapsed = false;
  try {
    collapsed = window.localStorage.getItem(storageKey) === 'true';
  } catch (_) {
    // The toggle also works when browser storage is unavailable.
  }

  const button = document.createElement('button');
  button.id = 'sidebar-collapse-toggle';
  button.type = 'button';
  button.setAttribute('aria-controls', 'sidebar');
  const icon = document.createElement('span');
  icon.setAttribute('aria-hidden', 'true');
  button.appendChild(icon);
  document.body.appendChild(button);

  const sync = () => {
    const isCollapsed = desktop.matches && collapsed;
    button.hidden = !desktop.matches;
    button.setAttribute('aria-expanded', String(!isCollapsed));
    const label = isCollapsed ? 'Show sidebar' : 'Hide sidebar';
    button.setAttribute('aria-label', label);
    button.title = label;
    icon.textContent = isCollapsed ? '☰' : '‹';
    if (isCollapsed && sidebar.contains(document.activeElement)) {
      button.focus({ preventScroll: true });
    }
    document.body.classList.toggle('sidebar-collapsed', isCollapsed);
    sidebar.inert = isCollapsed;
  };

  button.addEventListener('click', () => {
    if (!desktop.matches) return;
    collapsed = !collapsed;
    try {
      window.localStorage.setItem(storageKey, String(collapsed));
    } catch (_) {
      // Keep the current-page state even if it cannot be saved.
    }
    sync();
  });

  desktop.addEventListener('change', sync);
  sync();
})();
