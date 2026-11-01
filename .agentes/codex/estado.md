# Estado do projeto — Time Codex

Atualizado em: 2026-11-01 (America/Sao_Paulo)

## Objetivo atual

Manter o portfólio como site estático compatível com a Vercel, preservar o design editorial e apresentar corretamente a progressão profissional e a foto canônica do perfil.

## Entrega atual

- `index.html`: função atual `Logistics Specialist (Development)` desde SET/2026; trajetória Arilog segmentada em quatro etapas; hero atualizado; experiências anteriores preservadas.
- `style.css`: linha vertical contínua de progressão, nós por cargo, destaque da função atual e enquadramento responsivo da nova foto.
- `script.js`: sidebar recolhível com estado visual e atributos ARIA sincronizados no desktop, mobile, navegação e resize.
- `assets/foto_perfil.jpeg`: asset canônico da foto de perfil e do hero; o arquivo fornecido pelo usuário deve ser preservado.

## Verificações

- `node --check script.js`: passou.
- `git diff --check`: passou, apenas com aviso de futura normalização LF/CRLF.
- Render desktop no Edge: hero, nova foto e trajetória validados visualmente.
- Render mobile em 390x844: sem overflow horizontal; sidebar inicia recolhida e anuncia `aria-expanded=false` / `Expandir menu`.
- Revisão independente final: aprovada para commit/deploy.

## Execução do time

- Head `/root`: coordenação, integração, validação visual e memória; modelo da sessão selecionado no app; concluído.
- Software `/root/software_promocao`: papel `codex-software`; `index.html` e `script.js`; concluído.
- Designer `/root/design_trajetoria`: papel `codex-designer`; `style.css`; concluído.
- Revisor `/root/revisao_final`: papel `codex-revisor`; revisão independente; aprovado.

## Decisões duráveis

- O portfólio não usa Streamlit; é HTML/CSS/JavaScript estático para Vercel.
- A função atual desde SET/2026 é `Logistics Specialist (Development)`.
- A trajetória usa `.timeline`, `.job`, `.job-current` e `.career-track` como contrato visual e semântico.
- O estado acessível do menu deriva de `menu-open` no mobile e `collapsed` no desktop.

## Pendências

- Nenhuma pendência funcional conhecida neste patch.
