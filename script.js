const body = document.body;
const toggle = document.querySelector('#toggle');
const sidebar = document.querySelector('#sidebar');
const main = document.querySelector('main');
const skipLink = document.querySelector('.skip');
const links = [...document.querySelectorAll('nav a')];
const mobileQuery = matchMedia('(max-width: 760px)');
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const mobile = () => mobileQuery.matches;
const menuIsOpen = () => mobile() ? body.classList.contains('menu-open') : !body.classList.contains('collapsed');

const syncMenu = () => {
  const open = menuIsOpen();
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Recolher menu' : 'Expandir menu');
  sidebar.inert = !open;
  main.inert = mobile() && open;
  skipLink.inert = mobile() && open;
};

const closeMobileMenu = () => {
  if (!mobile() || !body.classList.contains('menu-open')) return;
  body.classList.remove('menu-open');
  syncMenu();
  toggle.focus();
};

body.classList.remove('menu-open');
syncMenu();

toggle.addEventListener('click', () => {
  body.classList.toggle(mobile() ? 'menu-open' : 'collapsed');
  syncMenu();
  if (mobile() && menuIsOpen()) sidebar.querySelector('a')?.focus();
});

links.forEach((link) => link.addEventListener('click', closeMobileMenu));
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeMobileMenu();
    return;
  }
  if (event.key !== 'Tab' || !mobile() || !menuIsOpen()) return;
  const focusable = [...sidebar.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'), toggle];
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  if (!focusable.includes(document.activeElement)) {
    event.preventDefault();
    (event.shiftKey ? last : first).focus();
  } else if (event.shiftKey && document.activeElement === first) {
    event.preventDefault();
    last.focus();
  } else if (!event.shiftKey && document.activeElement === last) {
    event.preventDefault();
    first.focus();
  }
});
document.addEventListener('pointerdown', (event) => {
  if (mobile() && menuIsOpen() && !sidebar.contains(event.target) && !toggle.contains(event.target)) closeMobileMenu();
});

const activeObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    links.forEach((link) => {
      const active = link.hash === `#${entry.target.id}`;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
  });
}, { rootMargin: '-30% 0px -60%' });
document.querySelectorAll('main section[id]').forEach((section) => activeObserver.observe(section));

if (reduceMotion) {
  document.querySelectorAll('.reveal').forEach((element) => element.classList.add('visible'));
} else {
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    });
  }, { threshold: .1 });
  document.querySelectorAll('.reveal').forEach((element) => revealObserver.observe(element));
}

document.querySelector('#year').textContent = new Date().getFullYear();
mobileQuery.addEventListener('change', () => {
  const focusWasInSidebar = sidebar.contains(document.activeElement);
  body.classList.remove('menu-open');
  syncMenu();
  if (sidebar.inert && focusWasInSidebar) toggle.focus();
});
