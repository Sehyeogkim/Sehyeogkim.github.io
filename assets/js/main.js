// ==========================================================================
// Sehyeog Kim Personal Blog — Main JavaScript
// Updated by AI Agent: 2026-02-26 07:55 KST — Dark/Light 토글 복원
// ==========================================================================
(function () {
  'use strict';

  // Theme toggle
  var saved = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);

  var themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var cur = document.documentElement.getAttribute('data-theme');
      var next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    });
  }

  // Mobile sidebar
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
      if (sidebar.classList.contains('open')) { closeMenu(); }
      else {
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
