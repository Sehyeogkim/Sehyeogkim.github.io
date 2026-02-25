// ==========================================================================
// Sehyeog Kim Personal Blog — Main JavaScript
// Rewritten by AI Agent: 2026-02-25 23:30 KST — 모바일 메뉴만 유지
// ==========================================================================
(function () {
  'use strict';
  var menuToggle = document.querySelector('.menu-toggle');
  var sidebar = document.querySelector('.sidebar');
  var overlay = document.querySelector('.sidebar-overlay');

  function closeMenu() {
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (menuToggle) {
    menuToggle.addEventListener('click', function () {
      if (sidebar.classList.contains('open')) {
        closeMenu();
      } else {
        sidebar.classList.add('open');
        overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  }

  if (overlay) { overlay.addEventListener('click', closeMenu); }

  document.querySelectorAll('.sidebar-nav .nav-item').forEach(function (link) {
    link.addEventListener('click', function () {
      if (window.innerWidth <= 768) { closeMenu(); }
    });
  });
})();
