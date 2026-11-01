const body=document.body,toggle=document.querySelector('#toggle'),links=[...document.querySelectorAll('nav a')],mobile=()=>matchMedia('(max-width:760px)').matches;
const syncMenuButton=()=>{const open=mobile()?body.classList.contains('menu-open'):!body.classList.contains('collapsed');toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Recolher menu':'Expandir menu')};
let wasMobile=mobile();if(wasMobile)body.classList.remove('menu-open');syncMenuButton();
toggle.addEventListener('click',()=>{body.classList.toggle(mobile()?'menu-open':'collapsed');syncMenuButton()});
links.forEach(a=>a.addEventListener('click',()=>{if(mobile())body.classList.remove('menu-open');syncMenuButton()}));
const activeObserver=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)links.forEach(a=>a.classList.toggle('active',a.hash===`#${e.target.id}`))}),{rootMargin:'-30% 0px -60%'});document.querySelectorAll('main section[id]').forEach(s=>activeObserver.observe(s));
const revealObserver=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');revealObserver.unobserve(e.target)}}),{threshold:.1});document.querySelectorAll('.reveal').forEach(e=>revealObserver.observe(e));
document.querySelector('#year').textContent=new Date().getFullYear();addEventListener('resize',()=>{const isMobile=mobile();if(isMobile!==wasMobile)body.classList.remove('menu-open');wasMobile=isMobile;syncMenuButton()});
