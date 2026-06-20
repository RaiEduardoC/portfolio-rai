import streamlit as st
from pathlib import Path
import base64
from PIL import Image

# ============================================================
# HELPERS DE ASSETS (devem vir antes de set_page_config)
# ============================================================
def get_page_icon():
    for name in ("assets/foto_perfil.jpg", "assets/foto_perfil.jpeg",
                 "assets/foto_perfil.png"):
        path = Path(__file__).parent / name
        if path.exists():
            return Image.open(path)
    return "📊"

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Raí Eduardo Cardoso | Analista de Dados",
    page_icon=get_page_icon(),
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CARREGAR CSS EXTERNO
# ============================================================
def load_css(file_name: str) -> None:
    css_path = Path(__file__).parent / file_name
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_photo_b64() -> str:
    for name in ("assets/foto_perfil.jpg", "assets/foto_perfil.jpeg",
                 "assets/foto_perfil.png", "foto_perfil.jpg",
                 "foto_perfil.jpeg", "foto_perfil.png"):
        path = Path(__file__).parent / name
        if path.exists():
            with open(path, "rb") as f:
                ext = path.suffix.lstrip(".").replace("jpg", "jpeg")
                return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode()}"
    return ""

def get_icon_b64(icon_name: str) -> str:
    path = Path(__file__).parent / "assets" / icon_name
    if path.exists():
        with open(path, "rb") as f:
            ext = path.suffix.lstrip(".")
            return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode()}"
    return ""

load_css("style.css")
FOTO_B64 = get_photo_b64()

# Ícones (Base64) — usados nos títulos, localização e cards de contato
HOME_ICON = get_icon_b64("home.png")
USER_ICON = get_icon_b64("user.png")
SUITCASE_ICON = get_icon_b64("suitcase.png")
GRADUATION_ICON = get_icon_b64("graduation.png")
COMPETENCIA_ICON = get_icon_b64("flash (1).png")
STARTUP_ICON = get_icon_b64("start-up.png")

LOCATION_ICON = get_icon_b64("localizacao.png")
LINKEDIN_ICON = get_icon_b64("linkedin.png")
GITHUB_ICON = get_icon_b64("github-logo.png")
GMAIL_ICON = get_icon_b64("gmail.png")
PHONE_ICON = get_icon_b64("telephone.png")
WHATSAPP_ICON = get_icon_b64("whatsapp.png")
PYTHON_ICON = get_icon_b64("python.png")

# Ícones do menu lateral: o st.radio não aceita HTML nas opções, então
# injetamos a imagem (Base64) via CSS ::before em cada item, na ordem do menu.
_MENU_ICONS = [HOME_ICON, SUITCASE_ICON, GRADUATION_ICON,
               COMPETENCIA_ICON, STARTUP_ICON, PHONE_ICON]
_menu_css = "".join(
    f'section[data-testid="stSidebar"] .stRadio [role="radiogroup"] '
    f'> label:nth-of-type({i + 1})::before {{ background-image: url("{icon}"); }}'
    for i, icon in enumerate(_MENU_ICONS) if icon
)
st.markdown(f"<style>{_menu_css}</style>", unsafe_allow_html=True)

# ============================================================
# DADOS DO PERFIL (centralizados para fácil manutenção)
# ============================================================
PERFIL = {
    "nome": "Raí Eduardo Cardoso",
    "cargo": "Analista de Dados Sênior | Logística & BI",
    "resumo": (
        "Analista de Dados com foco em Business Intelligence, automação "
        "de processos e desenvolvimento de soluções orientadas a dados. "
        "Atuo na construção de KPIs, OKRs, modelagem de dados, processos "
        "ETL e dashboards estratégicos que apoiam a tomada de decisão."
    ),
    "localizacao": "Maringá - PR, Brasil",
    "email": "raieduardocardoso@gmail.com",
    "telefone": "(44) 98447-3227",
    "linkedin": "https://www.linkedin.com/in/rai-eduardo-cardoso-356939259",
    "github": "https://github.com/RaiEduardoC",
}

EXPERIENCIAS = [
    {
        "cargo": "Analista de Dados – Sênior (Logística)",
        "empresa": "Arilog Soluções em Transporte",
        "local": "Paiçandu - PR",
        "periodo": "Maio/2025 — Atual",
        "descricao": (
            "Responsável pela análise de dados no setor de logística, com foco "
            "na criação de KPIs e OKRs voltados à otimização de processos e "
            "controle de custos. Desenvolvo análises estratégicas utilizando "
            "Oracle (PL/SQL), Power BI, Excel, VBA e Python. Estruturo e "
            "automatizo rotinas analíticas, criando painéis interativos e "
            "relatórios gerenciais."
        ),
        "tags": ["Oracle PL/SQL", "Power BI", "Python", "VBA", "KPIs", "OKRs"]
    },
    {
        "cargo": "Assistente de Inteligência de Transporte",
        "empresa": "Arilog Soluções em Transporte",
        "local": "Paiçandu - PR",
        "periodo": "Janeiro/2025 — Maio/2025",
        "descricao": (
            "Atuação na gestão e otimização de processos logísticos, com foco "
            "em eficiência operacional e suporte à tomada de decisão. "
            "Responsável pela formação de pagamento a terceiros, controle de "
            "coletas, embarques, monitoramento de entregas e validação de "
            "custos de rotas."
        ),
        "tags": ["Logística", "Excel", "Power BI", "Custos", "Análise"]
    },
    {
        "cargo": "Auxiliar de Transporte",
        "empresa": "Arilu",
        "local": "Maringá - PR",
        "periodo": "Março/2024 — Dezembro/2024",
        "descricao": (
            "Atualização de custos de manutenção semanal de caminhões, criação "
            "de planilhas em Excel e monitoramento de rotas e fluxo de "
            "entregas. Apoio em rotinas administrativas como preparação de "
            "contratos e controle de pagamentos."
        ),
        "tags": ["Excel", "Administrativo", "Logística", "Controle"]
    },
    {
        "cargo": "Jovem Aprendiz",
        "empresa": "Arilu",
        "local": "Maringá - PR",
        "periodo": "Fevereiro/2023 — Março/2024",
        "descricao": (
            "Atuação no setor de transporte e suporte, elaborando planilhas "
            "de entregas, médias de caminhões e controle de manutenção da frota."
        ),
        "tags": ["Excel", "Suporte", "Planilhas"]
    }
]

FORMACOES = [
    {
        "curso": "Graduação em Ciência de Dados",
        "instituicao": "Uninter",
        "periodo": "2025 — 2028",
        "status": "Cursando",
        "descricao": (
            "Modelagem de banco de dados, ETL/ELT, APIs, Aprendizado de Máquina, "
            "Big Data, Cloud, Visualização e BI, KPIs e storytelling."
        )
    },
    {
        "curso": "Técnico em Análise e Desenvolvimento de Sistemas",
        "instituicao": "Unicesumar",
        "periodo": "Concluído",
        "status": "Concluído",
        "descricao": (
            "Lógica de programação, algoritmos, sistemas operacionais, POO, "
            "bancos de dados e engenharia de software."
        )
    },
    {
        "curso": "Engenharia de Software",
        "instituicao": "Unicesumar",
        "periodo": "2025 — 2026",
        "status": "Trancado",
        "descricao": (
            "Fundamentos de computação, programação, lógica, sistemas "
            "operacionais, análise de dados, redes e gestão de software."
        )
    },
    {
        "curso": "Ensino Médio",
        "instituicao": "Colégio da Polícia Militar - Maringá",
        "periodo": "2018 — 2024",
        "status": "Concluído",
        "descricao": "Formação completa no ensino médio."
    }
]

CURSOS = [
    {
        "nome": "SQL Avançado (Oracle, SSMS, MySQL)",
        "escola": "Hashtag Treinamentos",
        "ano": "2025",
        "status": "Concluído",
        "icone": "🗃️"
    },
    {
        "nome": "Power BI Avançado",
        "escola": "Eduliv School Tec",
        "ano": "2023–2024",
        "status": "Concluído",
        "icone": "📊"
    },
    {
        "nome": "Excel e VBA Avançado",
        "escola": "Eduliv School Tec",
        "ano": "2022–2024",
        "status": "Concluído",
        "icone": "📈"
    },
    {
        "nome": "Python (Pandas, APIs, Automação)",
        "escola": "Hashtag Treinamentos",
        "ano": "2025",
        "status": "Cursando",
        "icone": "🐍"
    },
    {
        "nome": "Power Automate",
        "escola": "Hashtag Treinamentos",
        "ano": "2025–2026",
        "status": "Cursando",
        "icone": "⚙️"
    },
    {
        "nome": "Desenvolvimento IA e OpenClaw",
        "escola": "Hashtag Treinamentos",
        "ano": "2026",
        "status": "Cursando",
        "icone": "🤖"
    },
    {
        "nome": "Data Science (Análise, ETL, SQL, BI)",
        "escola": "Alex Lage Data Science / Anhanguera",
        "ano": "—",
        "status": "Concluído",
        "icone": "🧠"
    }
]

COMPETENCIAS = {
    "Linguagens & Bancos de Dados": [
        ("SQL (Oracle, SQL Server, MySQL)", 100),
        ("Python (Pandas, Streamlit, APIs)", 85),
        ("VBA", 100),
        ("DAX", 100),
    ],
    "Business Intelligence": [
        ("Power BI", 100),
        ("Excel Avançado", 100),
        ("Modelagem de Dados", 100),
        ("Storytelling com Dados", 100),
    ],
    "Engenharia de Dados & Automação": [
        ("ETL / Pipelines", 100),
        ("Power Automate", 100),
        ("Git & GitHub", 100),
        ("Integração via APIs", 100),
    ],
    "Inteligência Artificial": [
        ("Engenharia de Prompts", 85),
        ("Agentes Autônomos", 75),
        ("OpenClaw / Claude Code", 78),
    ]
}

PROJETOS = [
    {
        "titulo": "Portal Corporativo em Python + Streamlit",
        "descricao": (
            "Plataforma corporativa completa com autenticação de usuários, "
            "controle de acesso por permissões, integração com Google Sheets "
            "e Google Drive, exportação de relatórios e monitoramento de "
            "indicadores em tempo real."
        ),
        "tecnologias": ["Python", "Streamlit", "Google APIs", "Pandas"],
        "impacto": "Centralização de processos e ganho de produtividade."
    },
    {
        "titulo": "Otimização de Indicadores Logísticos",
        "descricao": (
            "Análise estratégica de dados para identificar pontos de melhoria "
            "em rotas e custos. Construção de KPIs e OKRs voltados a custo "
            "de frete, OTIF e eficiência operacional."
        ),
        "tecnologias": ["Power BI", "SQL", "DAX", "Excel"],
        "impacto": "Redução de 0,8% nos custos de frete e +15% no OTIF."
    },
    {
        "titulo": "Pipelines ETL e Dashboards Executivos",
        "descricao": (
            "Construção de processos ETL para abastecimento automático de "
            "dashboards gerenciais. Modelagem em estrela, tratamento via "
            "Power Query e relacionamentos otimizados."
        ),
        "tecnologias": ["Power BI", "Power Query", "SQL", "Python"],
        "impacto": "Automação completa de relatórios gerenciais."
    },
    {
        "titulo": "Automação de Processos Corporativos",
        "descricao": (
            "Desenvolvimento de fluxos automatizados utilizando Power Automate, "
            "VBA e Python, integrando aplicativos e serviços corporativos."
        ),
        "tecnologias": ["Power Automate", "VBA", "Python", "APIs"],
        "impacto": "Redução significativa de tarefas manuais."
    },
    {
        "titulo": "Aplicação de IA em Processos de Negócio",
        "descricao": (
            "Criação de agentes especializados, engenharia de prompts e "
            "orquestração multiagente com Claude Code e OpenClaw para "
            "automação inteligente de tarefas corporativas."
        ),
        "tecnologias": ["Claude Code", "OpenClaw", "Python", "APIs"],
        "impacto": "Maior produtividade e respostas inteligentes."
    },
    {
        "titulo": "Governança e Versionamento de Dados",
        "descricao": (
            "Estruturação, padronização e documentação de bases de dados "
            "do setor logístico. Organização de repositórios e controle "
            "de versões com Git/GitHub."
        ),
        "tecnologias": ["Git", "GitHub", "SQL", "Documentação"],
        "impacto": "Confiabilidade e rastreabilidade dos dados."
    }
]

# ============================================================
# COMPONENTES VISUAIS
# ============================================================
def render_header():
    avatar = (
        f'<img src="{FOTO_B64}" class="header-avatar photo" alt="Raí Eduardo Cardoso"/>'
        if FOTO_B64 else
        '<div class="header-avatar">RC</div>'
    )
    st.markdown(f"""
        <div class="header-container">
            {avatar}
            <div class="header-text">
                <h1 class="header-name">{PERFIL['nome']}</h1>
                <p class="header-role">{PERFIL['cargo']}</p>
                <p class="header-location">
                    <img src="{LOCATION_ICON}" class="icon"/>{PERFIL['localizacao']}
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_sobre():
    st.markdown(
        f"<h2 class='section-title'><img src='{USER_ICON}' class='icon-title'/>Sobre Mim</h2>",
        unsafe_allow_html=True)
    st.markdown(f"<div class='about-card'><p>{PERFIL['resumo']}</p></div>",
                unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        ("3+", "Anos de Experiência"),
        ("10+", "Cursos Concluídos"),
        ("15%", "Aumento OTIF"),
        ("0,8%", "Redução Custo Frete"),
    ]
    for col, (valor, label) in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{valor}</div>
                    <div class="metric-label">{label}</div>
                </div>
            """, unsafe_allow_html=True)

def render_experiencias():
    st.markdown(
        f"<h2 class='section-title'><img src='{SUITCASE_ICON}' class='icon-title'/>"
        "Experiência Profissional</h2>",
        unsafe_allow_html=True)
    for exp in EXPERIENCIAS:
        tags_html = "".join([f"<span class='tag'>{t}</span>" for t in exp["tags"]])
        st.markdown(f"""
            <div class="exp-card">
                <div class="exp-header">
                    <div>
                        <h3 class="exp-cargo">{exp['cargo']}</h3>
                        <p class="exp-empresa">{exp['empresa']} · {exp['local']}</p>
                    </div>
                    <span class="exp-periodo">{exp['periodo']}</span>
                </div>
                <p class="exp-descricao">{exp['descricao']}</p>
                <div class="tags-container">{tags_html}</div>
            </div>
        """, unsafe_allow_html=True)

def render_formacao():
    st.markdown(
        f"<h2 class='section-title'><img src='{GRADUATION_ICON}' class='icon-title'/>"
        "Formação Acadêmica</h2>",
        unsafe_allow_html=True)
    for f in FORMACOES:
        status_class = "status-cursando" if f["status"] == "Cursando" else \
                       "status-trancado" if f["status"] == "Trancado" else \
                       "status-concluido"
        st.markdown(f"""
            <div class="form-card">
                <div class="form-header">
                    <h3 class="form-curso">{f['curso']}</h3>
                    <span class="status-badge {status_class}">{f['status']}</span>
                </div>
                <p class="form-instituicao">{f['instituicao']} · {f['periodo']}</p>
                <p class="form-descricao">{f['descricao']}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 class='subsection-title'>📚 Cursos & Especializações</h3>",
                unsafe_allow_html=True)

    cols = st.columns(2)
    for i, c in enumerate(CURSOS):
        with cols[i % 2]:
            status_class = "status-cursando" if c["status"] == "Cursando" \
                           else "status-concluido"
            st.markdown(f"""
                <div class="curso-card">
                    <div class="curso-icone">{c['icone']}</div>
                    <div class="curso-info">
                        <h4>{c['nome']}</h4>
                        <p>{c['escola']} · {c['ano']}</p>
                        <span class="status-badge {status_class}">{c['status']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

def render_competencias():
    st.markdown(
        f"<h2 class='section-title'><img src='{COMPETENCIA_ICON}' class='icon-title'/>"
        "Competências Técnicas</h2>",
        unsafe_allow_html=True)
    for categoria, skills in COMPETENCIAS.items():
        st.markdown(f"<h3 class='skill-category'>{categoria}</h3>",
                    unsafe_allow_html=True)
        for skill, nivel in skills:
            st.markdown(f"""
                <div class="skill-item">
                    <div class="skill-header">
                        <span class="skill-name">{skill}</span>
                        <span class="skill-level">{nivel}%</span>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-fill" style="width: {nivel}%"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

def render_projetos():
    st.markdown(
        f"<h2 class='section-title'><img src='{STARTUP_ICON}' class='icon-title'/>"
        "Projetos &amp; Realizações</h2>",
        unsafe_allow_html=True)
    cols = st.columns(2)
    for i, p in enumerate(PROJETOS):
        with cols[i % 2]:
            techs = "".join([f"<span class='tech-pill'>{t}</span>"
                             for t in p["tecnologias"]])
            st.markdown(f"""
                <div class="projeto-card">
                    <h3 class="projeto-titulo">{p['titulo']}</h3>
                    <p class="projeto-descricao">{p['descricao']}</p>
                    <div class="tech-container">{techs}</div>
                    <div class="projeto-impacto">
                        <strong>💡 Impacto:</strong> {p['impacto']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

def render_contato():
    st.markdown(
        f"<h2 class='section-title'><img src='{GMAIL_ICON}' class='icon-title'/>"
        "Vamos Conversar?</h2>",
        unsafe_allow_html=True)
    st.markdown(f"""
        <div class="contato-container">
            <p class="contato-intro">
                Estou aberto a oportunidades, colaborações e novos desafios
                na área de <strong>Dados, BI e Automação</strong>.
            </p>
            <div class="contato-grid">
                <a href="mailto:{PERFIL['email']}" class="contato-card">
                    <div class="contato-icone"><img src="{GMAIL_ICON}" class="icon-contact"/></div>
                    <div class="contato-label">E-mail</div>
                    <div class="contato-valor">{PERFIL['email']}</div>
                </a>
                <a href="{PERFIL['linkedin']}" target="_blank" class="contato-card">
                    <div class="contato-icone"><img src="{LINKEDIN_ICON}" class="icon-contact"/></div>
                    <div class="contato-label">LinkedIn</div>
                    <div class="contato-valor">rai-eduardo-cardoso</div>
                </a>
                <a href="{PERFIL['github']}" target="_blank" class="contato-card">
                    <div class="contato-icone"><img src="{GITHUB_ICON}" class="icon-contact"/></div>
                    <div class="contato-label">GitHub</div>
                    <div class="contato-valor">RaiEduardoC</div>
                </a>
                <a href="https://wa.me/5544984473227" target="_blank" class="contato-card">
                    <div class="contato-icone"><img src="{WHATSAPP_ICON}" class="icon-contact"/></div>
                    <div class="contato-label">WhatsApp</div>
                    <div class="contato-valor">{PERFIL['telefone']}</div>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# SIDEBAR DE NAVEGAÇÃO
# ============================================================
with st.sidebar:
    sidebar_avatar = (
        f'<img src="{FOTO_B64}" class="sidebar-avatar photo" alt="Raí Eduardo Cardoso"/>'
        if FOTO_B64 else
        '<div class="sidebar-avatar">RC</div>'
    )
    st.markdown(f"""
        <div class="sidebar-profile">
            {sidebar_avatar}
            <h3>Raí E. Cardoso</h3>
            <p>Analista de Dados</p>
        </div>
    """, unsafe_allow_html=True)

    pagina = st.radio(
        "Navegação",
        ["Início", "Experiência", "Formação",
         "Competências", "Projetos", "Contato"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown(f"""
        <div class="sidebar-links">
            <a href="{PERFIL['linkedin']}" target="_blank">
                <img src="{LINKEDIN_ICON}" class="icon"/>LinkedIn
            </a>
            <a href="{PERFIL['github']}" target="_blank">
                <img src="{GITHUB_ICON}" class="icon"/>GitHub
            </a>
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# ROTEAMENTO DAS PÁGINAS
# ============================================================
render_header()
st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

if pagina == "Início":
    render_sobre()
elif pagina == "Experiência":
    render_experiencias()
elif pagina == "Formação":
    render_formacao()
elif pagina == "Competências":
    render_competencias()
elif pagina == "Projetos":
    render_projetos()
elif pagina == "Contato":
    render_contato()

# ============================================================
# RODAPÉ
# ============================================================
st.markdown(f"""
    <div class="footer">
        <p>© 2026 Raí Eduardo Cardoso — Desenvolvido com Python &amp; Streamlit
        <img src="{PYTHON_ICON}" class="icon icon-footer"/></p>
    </div>
""", unsafe_allow_html=True)