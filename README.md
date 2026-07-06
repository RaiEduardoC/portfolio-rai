# Portfólio Pessoal - Raí Eduardo Cardoso

Site de apresentação pessoal desenvolvido em **Python + Streamlit**, com tema dark personalizado.

## Sobre

Portfólio profissional com seções de experiência, formação acadêmica, competências técnicas, projetos e contato. Projetado para destacar a trajetória na área de **Análise de Dados, BI e Automação**.

## Tecnologias

- Python 3.10+
- Streamlit 1.43 (versão fixada — garante o mesmo comportamento local e na nuvem)
- HTML / CSS customizado (tema dark, glassmorphism, timeline)
- Cache nativo do Streamlit (`st.cache_data` / `st.cache_resource`) para assets e PDFs

## Como executar localmente

```bash
# Clone o repositório
git clone https://github.com/RaiEduardoC/portfolio-rai.git
cd portfolio-rai

# Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute o app
streamlit run app.py
```

## Deploy no Streamlit Community Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Conecte sua conta GitHub
3. Selecione o repositório `RaiEduardoC/portfolio-rai`
4. Branch: `main` | Arquivo principal: `app.py`
5. Clique em **Deploy**
