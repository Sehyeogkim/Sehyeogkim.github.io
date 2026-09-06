(() => {
  'use strict';
  document.querySelectorAll('[data-journal]').forEach((root) => {
    const cards = Array.from(root.querySelectorAll('[data-journal-card]'));
    const tools = root.querySelector('.journal-tools');
    const input = root.querySelector('[data-journal-search]');
    const status = root.querySelector('[data-journal-status]');
    const more = root.querySelector('[data-journal-more]');
    const empty = root.querySelector('[data-journal-empty]');
    if (!cards.length || !tools || !input || !status || !more || !empty) return;
    const pageSize = 24;
    let limit = pageSize;
    const normalize = (value) => value.normalize('NFKC').toLocaleLowerCase();
    const render = () => {
      const words = normalize(input.value).trim().split(/\s+/).filter(Boolean);
      let count = 0;
      cards.forEach((card) => {
        const matches = words.every((word) => normalize(card.dataset.search || '').includes(word));
        if (matches) count += 1;
        card.hidden = !matches || count > limit;
      });
      status.textContent = `${Math.min(count, limit)} / ${count} notes`;
      more.hidden = count <= limit;
      empty.hidden = count !== 0;
    };
    input.addEventListener('input', () => { limit = pageSize; render(); });
    more.addEventListener('click', () => {
      const firstHidden = cards.find((card) => card.hidden && normalize(input.value).trim().split(/\s+/).filter(Boolean).every((word) => normalize(card.dataset.search || '').includes(word)));
      limit += pageSize;
      render();
      if (firstHidden) firstHidden.querySelector('h2 a')?.focus({preventScroll: true});
    });
    tools.hidden = false;
    render();
  });
  document.querySelectorAll('.journal-image-link img').forEach((img) => {
    const recover = () => {
      const teaser = img.parentElement;
      teaser.classList.add('journal-placeholder');
      const label = document.createElement('span');
      label.textContent = img.closest('[data-journal-card]').querySelector('.journal-card-meta').textContent.trim().split(/\s+/)[0];
      teaser.replaceChildren(label);
    };
    if (img.complete && img.naturalWidth === 0) recover();
    else img.addEventListener('error', recover, {once: true});
  });
})();
