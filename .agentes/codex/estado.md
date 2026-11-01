# Estado do projeto — Time Codex

Atualizado em: 2026-11-01 (America/Sao_Paulo)

## Objetivo atual

Elevar o portfólio Streamlit para apresentação profissional, revisar perfil e experiências sem inventar fatos, criar hero editorial com a foto, remover o ícone de "Sobre Mim" e preservar o recolhimento/expansão da sidebar.

## Entrega

- `app.py`: textos profissionais revisados; hero usa `assets/foto_perfil.jpeg` em `<img class="hero-profile-bg">`; "Sobre Mim" sem ícone; navegação preservada.
- `style.css`: hero editorial responsivo, overlays, hierarquia e acabamento de cards; controle nativo da sidebar visível; fallback sem foto.
- O HTML do hero deve permanecer sem indentação inicial para não virar bloco de código Markdown no Streamlit.

## Verificações do patch atual

- `py -3.12 -m py_compile app.py`: passou em 2026-11-01.
- `git diff --check`: passou em 2026-11-01.
- Streamlit AppTest: zero exceções; CTAs/navegação verificados pelo revisor.
- Teste visual desktop no Edge: hero/foto/overlay legíveis; sidebar recolheu e reabriu pelo controle nativo.
- Mobile: breakpoints 768/480 revisados estruturalmente, sem emulação visual.
- Revisão independente final: aprovada.

## Execução do time

- Head `/root`: modelo da sessão selecionado no app (a skill não o alterou); coordenação, integração, correções e testes; 2026-11-01; concluído.
- Designer `/root/design_portfolio`: papel `codex-designer`, modelo fixado pelo agente nativo em gpt-5.6-sol; `style.css` e validação visual; 2026-11-01; concluído.
- Software `/root/software_portfolio`: papel `codex-software`, modelo fixado pelo agente nativo em gpt-5.6-sol; `app.py`, correções do hero e testes; 2026-11-01; concluído.
- Revisor `/root/revisao_portfolio`: papel `codex-revisor`, modelo fixado pelo agente nativo em gpt-5.6-sol; revisão independente e AppTest; 2026-11-01; aprovado.

## Pendências

- Validar visualmente em viewport mobile real quando conveniente.
- Mudanças locais ainda não commitadas: `app.py` e `style.css`.
