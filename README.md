# Sistema de Geração de Relatórios com IA para Análise de Dados 🤖📊

## Visão Geral 🌍

Relatórios de dados são ferramentas essenciais para transformar dados brutos em informações compreensíveis e acionáveis. Eles ajudam a identificar tendências, padrões e anomalias, auxiliando na tomada de decisões estratégicas em diversas áreas. Este projeto visa simplificar e automatizar a criação desses relatórios, tornando a análise de dados acessível a todos, mesmo sem conhecimento técnico profundo em programação ou estatística.

Este sistema, desenvolvido como parte do curso de **Especialização Lato Sensu em Sistemas e Agentes Inteligentes** da **Universidade Federal de Goiás**, é uma aplicação web construída com o framework **Django** que permite processar e analisar dados de arquivos CSV de forma eficiente. Ele utiliza **Inteligência Artificial**, através da **API Google Gemini**, para gerar relatórios interativos e detalhados, fornecendo insights automatizados sobre os dados. Com uma interface intuitiva e responsiva, o sistema permite que usuários de qualquer nível de experiência possam carregar seus dados, obter análises completas e tomar decisões informadas de maneira rápida e fácil.

**Utilidade do Sistema:**

Este sistema é ideal para uma ampla gama de usuários e aplicações, incluindo:

*   **Analistas de dados:** Para acelerar a análise exploratória de dados (EDA) e gerar relatórios preliminares.
*   **Pesquisadores:** Para analisar dados de pesquisas, experimentos e estudos de forma rápida e eficiente.
*   **Estudantes:** Para aprender sobre análise de dados e praticar com conjuntos de dados reais.
*   **Profissionais de negócios:** Para obter insights sobre vendas, marketing, finanças e outras áreas.
*   **Gestores:** Para monitorar o desempenho de equipes, projetos e processos.
*   **Tomadores de decisão:** Para embasar decisões estratégicas com dados concretos.
*   **Desenvolvedores:** O sistema é extensível e customizável, permitindo que desenvolvedores adicionem novas funcionalidades, integrem com outras ferramentas e adaptem o sistema para necessidades específicas.

O sistema automatiza o processo de análise exploratória de dados (EDA) e geração de relatórios, economizando tempo e permitindo que os usuários foquem na interpretação dos resultados e tomada de decisões. O sistema é **totalmente responsivo**, garantindo acesso e usabilidade em diversos dispositivos, como computadores, tablets e smartphones.

## Tecnologias Utilizadas 🔧

- **Backend**:
  - [Django 5.1.5](https://www.djangoproject.com/): Framework web robusto e flexível para Python.
  - [Python 3.x](https://www.python.org/): Linguagem de programação versátil e poderosa.
  - [Pandas](https://pandas.pydata.org/) e [NumPy](https://numpy.org/): Bibliotecas para análise e manipulação de dados.
  - [Google Gemini API](https://ai.google.dev/): Para geração de insights automatizados com IA.
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/): Para gerenciamento de variáveis de ambiente.
  - **Modelo utilizado**: `gemini-exp-1206` (suporta até 2.097.152 tokens).

- **Frontend**:
  - HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/): Para criação de interfaces web responsivas e modernas.
  - JavaScript: Para interatividade e dinamismo no frontend.
  - [GitHub Markdown CSS](https://github.com/sindresorhus/github-markdown-css): Para exibição de relatórios em formato Markdown.

## Estrutura do Projeto 📂

```plaintext
myanalytics/
│── analytics/          # App principal do Django
│   │── migrations/     # Migrações do banco de dados
│   │── static/         # Arquivos estáticos (CSS, JS, imagens)
│   │   │── analytics/
│   │   │   │── css/
│   │   │   │── js/
│   │   │   │── images/
│   │── templates/analytics/  # Templates HTML
│   │   │── base.html       # Template base
│   │── admin.py          # Configuração do painel administrativo
│   │── apps.py           # Configuração do app
│   │── models.py         # Modelos de dados (estrutura do banco de dados)
│   │── services.py      # Lógica de negócios e operações
│   │── tests.py          # Testes unitários
│   │── urls.py           # Mapeamento de URLs para views
│   │── views.py          # Views (lógica de apresentação)
│── media/              # Diretório para arquivos enviados (CSV)
│── myanalytics/         # Configurações do projeto Django
│   │── __init__.py
│   │── asgi.py
│   │── settings.py      # Configurações (banco de dados, apps, etc.)
│   │── urls.py           # Mapeamento de URLs do projeto
│   │── wsgi.py
│── venv/               # Ambiente virtual (opcional, mas recomendado)
│── .env                # Arquivo de variáveis de ambiente
│── .gitignore          # Arquivos e diretórios ignorados pelo Git
│── db.sqlite3          # Banco de dados SQLite (padrão)
│── manage.py           # Script para executar comandos do Django
│── README.md           # Este arquivo
│── requirements.txt    # Lista de dependências do projeto
```

## Como Configurar e Executar o Projeto 🚀

**Pré-requisitos:**

Antes de começar, você precisa ter instalado em sua máquina:

-   **Git:** Para clonar o repositório do projeto. Você pode baixar e instalar o Git em [https://git-scm.com/](https://git-scm.com/).
-   **Python:** Certifique-se de ter o Python 3.x instalado. Você pode baixar a versão mais recente em [https://www.python.org/downloads/](https://www.python.org/downloads/). Recomenda-se usar o Python 3.9 ou superior.

### 1. Instalação e Configuração do Ambiente Virtual

Clone o repositório do projeto e navegue até a pasta:

```bash
git clone https://github.com/Carcalto/gerador-relatorio-dados-django-trab02-UFG.git
cd gerador-relatorio-dados-django-trab02-UFG
```

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 2. Instalação das Dependências do Projeto

Instale as bibliotecas Python necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google Gemini:

```env
GOOGLE_GEMINI_API_KEY=suachaveapi
```

**Como obter a chave da API do Google Gemini:**

1.  Acesse o site do [Google AI Studio](https://ai.google.dev/).
2.  Faça login com sua conta do Google.
3.  Crie um novo projeto ou selecione um projeto existente.
4.  Gere uma nova chave de API.
5.  Copie a chave e cole no arquivo `.env`.

### 4. Executar Migrações no Banco de Dados

O Django utiliza um banco de dados para armazenar informações sobre os uploads de arquivos e outros dados do sistema. Por padrão, o projeto usa o SQLite, um banco de dados leve que não requer configuração adicional. Para criar as tabelas necessárias no banco de dados, execute:

```bash
python manage.py migrate
```

### 5. (Opcional) Criar um Superusuário

Para acessar o painel administrativo do Django, você pode criar um superusuário:

```bash
python manage.py createsuperuser
```

Siga as instruções para definir um nome de usuário e senha.

### 6. Iniciar o Servidor Django

```bash
python manage.py runserver
```

Acesse o sistema em [http://localhost:8000](http://localhost:8000).

### 7. (Opcional) Coletar arquivos estáticos

Se você for implantar o projeto em um servidor de produção, é recomendado coletar os arquivos estáticos em um único diretório:

```bash
python manage.py collectstatic
```

## Fluxo de Funcionamento Detalhado ⏳

1.  **Upload e Validação do Arquivo CSV** 📤

    -   O usuário acessa a página inicial do sistema e seleciona um arquivo CSV para upload através de um formulário.
    -   O sistema recebe o arquivo enviado e realiza validações iniciais para garantir que o arquivo seja um CSV válido e não esteja vazio.
    -   Verifica se o arquivo possui uma estrutura adequada (colunas, separadores, etc.).
    -   Arquivos inválidos geram mensagens de erro apropriadas, informando o usuário sobre o problema.

    ```python
    # analytics/views.py
    def upload_csv(request):
        if request.method == 'POST' and request.FILES.get('csv_file'):
            csv_file = request.FILES['csv_file']

            # Validações básicas
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Erro: O arquivo deve ser um CSV.')
                return render(request, 'analytics/upload.html')

            try:
                df_original = pd.read_csv(csv_file)
            except FileNotFoundError:
                messages.error(request, "Erro: O arquivo não foi encontrado.")
                return render(request, 'analytics/upload.html')
            except pd.errors.EmptyDataError:
                messages.error(request, "Erro: O arquivo CSV está vazio.")
                return render(request, 'analytics/upload.html')
            except pd.errors.ParserError:
                messages.error(request, "Erro: Problema ao analisar o arquivo CSV.")
                return render(request, 'analytics/upload.html')

            # ... (restante do código) ...
    ```

2.  **Limpeza e Pré-processamento** 🔄

    -   Após a validação, o sistema realiza a limpeza e o pré-processamento dos dados para garantir a qualidade e consistência das informações.
    -   **Remoção de duplicatas:** Linhas duplicadas são identificadas e removidas do DataFrame.
    -   **Tratamento de valores nulos:** Valores ausentes (NaN) são preenchidos utilizando estratégias adequadas para cada tipo de coluna:
        *   **Colunas numéricas:** A mediana dos valores da coluna é utilizada para preencher os valores nulos.
        *   **Colunas categóricas:** A moda (valor mais frequente) da coluna é utilizada para preencher os valores nulos.
    -   **Remoção de colunas irrelevantes:** Colunas que não contêm informações relevantes para a análise, como colunas com nomes contendo "unnamed" (geradas em alguns casos durante a leitura de arquivos CSV), são removidas.

    ```python
    # analytics/services.py
    def validar_e_limpar_dados(df):
        """
        Valida e limpa o DataFrame fornecido.

        Args:
            df (pd.DataFrame): O DataFrame original.

        Returns:
            pd.DataFrame: O DataFrame limpo e validado.
        """
        df = df.drop_duplicates()  # Remove linhas duplicadas

        colunas_numericas = df.select_dtypes(include=['number']).columns
        for col in colunas_numericas:
            df[col] = df[col].fillna(df[col].median())  # Preenche NaN com a mediana

        colunas_categoricas = df.select_dtypes(include=['object']).columns
        for col in colunas_categoricas:
            df[col] = df[col].fillna(df[col].mode()[0])  # Preenche NaN com a moda

        df = df.drop(columns=[col for col in df.columns if 'unnamed' in col.lower()])  # Remove colunas "unnamed"

        return df
    ```

3. **Geração do Prompt para a IA** 🤖
   - Com os dados limpos e pré-processados, o sistema gera um prompt detalhado e contextualizado para ser enviado à API do Google Gemini.
   - O prompt é construído de forma a fornecer informações relevantes sobre os dados, incluindo:
       - Uma descrição do processo de limpeza realizado (quais colunas foram tratadas, como os valores nulos foram preenchidos, etc.).
        - As primeiras linhas do DataFrame limpo (usando `df.head().to_string()`), para que a IA tenha uma amostra dos dados.
        - Estatísticas descritivas das colunas (média, desvio padrão, mínimo, máximo, quartis), se relevantes.
        - Instruções claras para a IA sobre o que se espera dela (gerar insights, identificar padrões, sugerir visualizações, etc.).

    ```python
     # analytics/services.py
    def gerar_prompt(df_original, df_limpo):
        """
        Gera um prompt para o modelo Gemini, incluindo informações sobre a limpeza e os dados.

        Args:
            df_original (pd.DataFrame): DataFrame original.
            df_limpo (pd.DataFrame): DataFrame após a limpeza.

        Returns:
            str: O prompt gerado.
        """

        descricao_limpeza = gerar_descricao_limpeza(df_original, df_limpo)

        prompt = (
            "Você é um analista de dados experiente. Sua tarefa é analisar o conjunto de dados fornecido e gerar um relatório detalhado com insights relevantes.\n\n"
            "**Processo de Limpeza e Pré-processamento:**\n"
            f"{descricao_limpeza}\n\n"
            "**Amostra dos Dados (Primeiras Linhas):**\n"
            f"{df_limpo.head().to_string()}\n\n"
            "**Instruções:**\n"
            "- Identifique padrões, tendências e anomalias nos dados.\n"
            "- Forneça insights detalhados sobre as relações entre as variáveis.\n"
            "- Sugira visualizações (gráficos) que podem ajudar a ilustrar os dados e os insights.\n"
            "- Seja conciso e objetivo, mas forneça informações relevantes para um analista de dados.\n"
            "- Formate o relatório em Markdown para facilitar a leitura.\n"

        )
        return prompt

    def gerar_descricao_limpeza(df_original, df_limpo):
        """Gera uma descrição textual do processo de limpeza realizado."""

        num_duplicatas = df_original.duplicated().sum()
        descricao = f"- {num_duplicatas} linhas duplicadas foram removidas.\n"

        for col in df_original.columns:
            if df_original[col].isnull().any():
                if col in df_limpo.columns:  # Verifica se a coluna ainda existe
                    if df_limpo[col].dtype == 'number':
                        descricao += f"- Valores nulos na coluna '{col}' foram preenchidos com a mediana ({df_limpo[col].median():.2f}).\n"
                    else:
                        descricao += f"- Valores nulos na coluna '{col}' foram preenchidos com a moda ('{df_limpo[col].mode()[0]}').\n"

        colunas_removidas = [col for col in df_original.columns if 'unnamed' in col.lower()]
        if colunas_removidas:
            descricao += f"- As seguintes colunas irrelevantes foram removidas: {', '.join(colunas_removidas)}.\n"

        return descricao
    ```

    ```python
     # analytics/services.py
    def gerar_prompt(df_original, df_limpo):
        """
        Gera um prompt para o modelo Gemini, incluindo informações sobre a limpeza e os dados.

        Args:
            df_original (pd.DataFrame): DataFrame original.
            df_limpo (pd.DataFrame): DataFrame após a limpeza.

        Returns:
            str: O prompt gerado.
        """

        descricao_limpeza = gerar_descricao_limpeza(df_original, df_limpo)

        prompt = (
            "Você é um analista de dados experiente. Sua tarefa é analisar o conjunto de dados fornecido e gerar um relatório detalhado com insights relevantes.\n\n"
            "**Processo de Limpeza e Pré-processamento:**\n"
            f"{descricao_limpeza}\n\n"
            "**Amostra dos Dados (Primeiras Linhas):**\n"
            f"{df_limpo.head().to_string()}\n\n"
            "**Instruções:**\n"
            "- Identifique padrões, tendências e anomalias nos dados.\n"
            "- Forneça insights detalhados sobre as relações entre as variáveis.\n"
            "- Sugira visualizações (gráficos) que podem ajudar a ilustrar os dados e os insights.\n"
            "- Seja conciso e objetivo, mas forneça informações relevantes para um analista de dados.\n"
            "- Formate o relatório em Markdown para facilitar a leitura.\n"

        )
        return prompt

    def gerar_descricao_limpeza(df_original, df_limpo):
        """Gera uma descrição textual do processo de limpeza realizado."""

        num_duplicatas = df_original.duplicated().sum()
        descricao = f"- {num_duplicatas} linhas duplicadas foram removidas.\n"

        for col in df_original.columns:
            if df_original[col].isnull().any():
                if col in df_limpo.columns:  # Verifica se a coluna ainda existe
                    if df_limpo[col].dtype == 'number':
                        descricao += f"- Valores nulos na coluna '{col}' foram preenchidos com a mediana ({df_limpo[col].median():.2f}).\n"
                    else:
                        descricao += f"- Valores nulos na coluna '{col}' foram preenchidos com a moda ('{df_limpo[col].mode()[0]}').\n"

        colunas_removidas = [col for col in df_original.columns if 'unnamed' in col.lower()]
        if colunas_removidas:
            descricao += f"- As seguintes colunas irrelevantes foram removidas: {', '.join(colunas_removidas)}.\n"

        return descricao
    ```

4.  **Envio para o Modelo Google Gemini** 📡

    -   O prompt gerado, juntamente com os dados limpos (opcionalmente, dependendo do tamanho dos dados e da capacidade do modelo), é enviado para a API do Google Gemini.
    -   O modelo `gemini-exp-1206` é utilizado para processar o prompt e gerar os insights.
    -   A resposta da API, contendo os insights gerados pela IA, é recebida pelo sistema.

    ```python
    # analytics/services.py
    import google.generativeai as genai
    from dotenv import load_dotenv
    import os

    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

    def gerar_insights_gemini(prompt):
        """
        Envia o prompt para o modelo Gemini e retorna os insights gerados.

        Args:
            prompt (str): O prompt a ser enviado.

        Returns:
            str: Os insights gerados pelo modelo.
        """
        model = genai.GenerativeModel(model_name="gemini-exp-1206")
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro ao gerar insights com o Gemini: {e}"

    ```

5.  **Criação e Exibição do Relatório** 📜

    -   A resposta da API do Google Gemini, que contém os insights em formato de texto, é processada e formatada para exibição no frontend.
    -   O relatório final é gerado em formato Markdown, um formato de marcação leve que permite uma formatação simples e legível.
    -   O relatório inclui:
        *   Os insights gerados pela IA.
        *   Sugestões de visualizações (gráficos) que podem ajudar a ilustrar os dados e os insights.
        *   (Opcionalmente) Tabelas com estatísticas descritivas dos dados.
    -   O relatório em Markdown é convertido para HTML usando a biblioteca `markdown` do Python.
    -   O HTML gerado é renderizado em um template do Django (`analytics/templates/analytics/report.html`) e exibido ao usuário.

    ```python
    # analytics/services.py
    import markdown

    def gerar_relatorio(insights):
        """
        Converte os insights (em Markdown) para HTML.

        Args:
            insights (str): Os insights em formato Markdown.

        Returns:
            str: O relatório em formato HTML.
        """
        html = markdown.markdown(insights)
        return html

    # analytics/views.py
    def show_report(request):
        # ... (código anterior para upload, validação, limpeza) ...

        prompt = gerar_prompt(df_original, df_limpo)
        insights = gerar_insights_gemini(prompt)
        relatorio_html = gerar_relatorio(insights)

        return render(request, 'analytics/report.html', {'report': relatorio_html})
    ```

    **Exibição no Frontend (HTML, CSS, JavaScript):**

    O frontend do sistema é construído com HTML, CSS (Bootstrap 5) e JavaScript. A página de upload (`analytics/templates/analytics/upload.html`) contém um formulário para o envio do arquivo CSV. Após o processamento, o relatório gerado é exibido na página de relatório (`analytics/templates/analytics/report.html`). O CSS do GitHub Markdown é utilizado para estilizar o relatório em Markdown, proporcionando uma aparência limpa e profissional. O JavaScript é utilizado para interações básicas, como a exibição de mensagens de erro e sucesso.

## Comandos `manage.py` ⚙️

O script `manage.py` fornece vários comandos úteis para gerenciar o projeto Django:

*   `python manage.py runserver`: Inicia o servidor de desenvolvimento.
*   `python manage.py migrate`: Aplica as migrações do banco de dados.
*   `python manage.py createsuperuser`: Cria um superusuário para acessar o painel administrativo.
*   `python manage.py collectstatic`: Coleta os arquivos estáticos para implantação.
*   `python manage.py makemigrations`: Cria novas migrações com base nas alterações nos modelos.
*  `python manage.py shell`: Abre um shell interativo do Python com o contexto do Django.
*   `python manage.py test`: Executa os testes do projeto.

## Equipe 👨‍👩‍👦

- **Celio Oliveira Carcalto** - Matrícula: 2024201158
- **Anahi Philbois** - Matrícula: 2024201159

## Referência ao Curso 🎓

- **Universidade Federal de Goiás**
- **Especialização Lato Sensu: Sistemas e Agentes Inteligentes**
  - [Mais informações](https://agentes.inf.ufg.br/)

## Licença 🔒

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://opensource.org/licenses/MIT) para mais detalhes.

---

📌 **Nota:** O sistema é responsivo e pode ser acessado em qualquer dispositivo! 🚀
