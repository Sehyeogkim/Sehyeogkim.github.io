(() => {
  'use strict';

  const root = document.querySelector('[data-feed]');
  const filters = document.querySelector('[data-feed-filters]');
  if (!root || !filters) return;

  const cards = Array.from(root.querySelectorAll('[data-feed-card]'));
  const more = root.querySelector('[data-feed-more]');
  const empty = root.querySelector('[data-feed-empty]');
  const links = Array.from(filters.querySelectorAll('[data-filter]'));
  const pageSize = 24;
  let limit = pageSize;
  let active = new URLSearchParams(location.search).get('category') || 'all';
  if (!links.some((link) => link.dataset.filter === active)) active = 'all';

  const render = () => {
    let count = 0;
    cards.forEach((card) => {
      const matches = active === 'all' || card.dataset.category === active;
      if (matches) count += 1;
      card.hidden = !matches || count > limit;
    });
    links.forEach((link) => {
      if (link.dataset.filter === active) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
    more.hidden = count <= limit;
    empty.hidden = count !== 0;
  };

  links.forEach((link) => {
    link.addEventListener('click', (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.button !== 0) return;
      event.preventDefault();
      active = link.dataset.filter;
      limit = pageSize;
      history.replaceState(null, '', link.href);
      render();
    });
  });

  more.addEventListener('click', () => {
    limit += pageSize;
    render();
  });

  render();
})();
