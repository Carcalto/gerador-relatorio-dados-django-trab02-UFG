# Sistema de Geração de Relatórios com IA para Análise de Dados 🤖📊

## Visão Geral 🌍

Este projeto faz parte do curso de **Especialização Lato Sensu em Sistemas e Agentes Inteligentes** da **Universidade Federal de Goiás**. Criado com **Django**, o sistema processa dados de arquivos CSV e gera relatórios interativos enriquecidos com **Inteligência Artificial**, utilizando a **API Google Gemini** para fornecer insights automatizados. O sistema é **totalmente responsivo**, podendo ser acessado de qualquer dispositivo.

## Tecnologias Utilizadas 🔧

- **Backend**:
  - Django 5.1.5
  - Python 3.x
  - Pandas e NumPy (para análise de dados)
  - Google Gemini API (para insights automatizados)
  - `python-dotenv` (para gerenciamento de variáveis de ambiente)
  - **Modelo utilizado**: `gemini-exp-1206` (suporta até 2.097.152 tokens)

- **Frontend**:
  - HTML5, CSS3, Bootstrap 5
  - JavaScript
  - GitHub Markdown CSS (para exibição de relatórios)

## Estrutura do Projeto 📂

```plaintext
myanalytics/
│── analytics/
│   │── migrations/
│   │── static/
│   │── templates/analytics/
│   │   │── base.html
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── services.py
│   │── tests.py
│   │── urls.py
│   │── views.py
│── media/
│── myanalytics/
│   │── __init__.py
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── venv/
│── .env
│── .gitignore
│── db.sqlite3
│── manage.py
│── README.md
│── requirements.txt
```

## Como Configurar e Executar o Projeto 🚀

### 1. Instalação das Dependências

```bash
git clone https://github.com/Carcalto/gerador-relatorio-dados-django-trab02-UFG.git
cd gerador-relatorio-dados-django-trab02-UFG
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione:

```env
GOOGLE_GEMINI_API_KEY=suachaveapi
```

### 3. Executar Migrações no Banco de Dados

```bash
python manage.py migrate
```

### 4. Iniciar o Servidor Django

```bash
python manage.py runserver
```

Acesse o sistema em [http://localhost:8000](http://localhost:8000).

## Fluxo de Funcionamento Detalhado ⏳

1. **Upload e Validação do Arquivo CSV** 📤
   - O sistema recebe o arquivo CSV enviado pelo usuário.
   - Validações incluem verificar duplicatas e estrutura do arquivo.
   - Arquivos inválidos geram mensagens de erro apropriadas.

   ```python
   try:
       df_original = pd.read_csv(file_path)
   except FileNotFoundError:
       return "Erro: O arquivo não foi encontrado."
   except pd.errors.EmptyDataError:
       return "Erro: O arquivo CSV está vazio."
   except pd.errors.ParserError:
       return "Erro: Problema ao analisar o arquivo CSV."
   ```

2. **Limpeza e Pré-processamento** 🔄
   - Dados duplicados são removidos.
   - Valores nulos são tratados com mediana para colunas numéricas e moda para categóricas.
   - Colunas irrelevantes, como `Unnamed`, são descartadas.

   ```python
   def validar_e_limpar_dados(df):
       df = df.drop_duplicates()
       colunas_numericas = df.select_dtypes(include=['number']).columns
       for col in colunas_numericas:
           df[col] = df[col].fillna(df[col].median())
       colunas_categoricas = df.select_dtypes(include=['object']).columns
       for col in colunas_categoricas:
           df[col] = df[col].fillna(df[col].mode()[0])
       df = df.drop(columns=[col for col in df.columns if 'unnamed' in col.lower()])
       return df
   ```

3. **Geração do Prompt para a IA** 🤖
   - O sistema cria um prompt técnico e detalhado que descreve os dados.
   - Estatísticas descritivas e informações relevantes são incluídas no prompt para melhor interpretação pela IA.

   ```python
   descricao_limpeza = gerar_descricao_limpeza(df_original, df_limpo)
   prompt = (
       "Você é um analista de dados. Forneça insights detalhados sobre os dados abaixo:\n"
       f"{descricao_limpeza}\n"
       f"{df_limpo.head().to_string()}"
   )
   ```

4. **Envio para o Modelo Google Gemini** 📡
   - O modelo `gemini-exp-1206` processa o prompt juntamente com os dados limpos.
   - Insights detalhados são gerados, incluindo padrões, outliers e recomendações.

   ```python
   model = genai.GenerativeModel(model_name="gemini-exp-1206")
   insights = model.generate_content(prompt)
   ```

5. **Criação e Exibição do Relatório** 📜
   - O relatório final é formatado em Markdown para exibição amigável.
   - Inclui estatísticas, gráficos sugeridos e insights detalhados.

   ```python
   def gerar_relatorio(insights):
       return markdown.markdown(insights)
   ```

## Equipe 👨‍👩‍👦

- **Celio Oliveira Carcalto** - Matrícula: 2024201158
- **Anahi Philbois** - Matrícula: 2024201159

## Referência ao Curso 🎓

- **Universidade Federal de Goiás**
- **Especialização Lato Sensu: Sistemas e Agentes Inteligentes**
  - [Mais informações](https://agentes.inf.ufg.br/)

## Licença 🔒

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

📌 **Nota:** O sistema é responsivo e pode ser acessado em qualquer dispositivo! 🚀

