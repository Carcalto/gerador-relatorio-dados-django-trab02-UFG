import pandas as pd
import google.generativeai as genai
import os
from tqdm import tqdm

# Configurar a API do Google Gemini
api_key = os.getenv('GOOGLE_GEMINI_API_KEY')

if not api_key:
    raise ValueError(
        "A chave da API do Google Gemini não foi configurada. Configure a variável de ambiente GOOGLE_GEMINI_API_KEY.")

genai.configure(api_key=api_key)  # Configura a API com a chave

# Função para validar e limpar os dados


def validar_e_limpar_dados(df):
    # Remover duplicatas
    df = df.drop_duplicates()

    # Identificar colunas numéricas e categóricas
    colunas_numericas = df.select_dtypes(include=['number']).columns.tolist()
    colunas_categoricas = df.select_dtypes(
        include=['object', 'category']).columns.tolist()

    # Preencher valores ausentes nas colunas numéricas com a mediana
    for col in colunas_numericas:
        if df[col].isnull().any():
            mediana = df[col].median()
            df[col] = df[col].fillna(mediana)

    # Preencher valores ausentes nas colunas categóricas com a moda
    for col in colunas_categoricas:
        if df[col].isnull().any():
            moda = df[col].mode()[0]
            df[col] = df[col].fillna(moda)

    # Remover colunas com nomes genéricos como 'Unnamed'
    colunas_para_remover = [
        col for col in df.columns if 'unnamed' in col.lower()]
    if colunas_para_remover:
        df = df.drop(columns=colunas_para_remover)

    return df

# Função para gerar a descrição das etapas de limpeza


def gerar_descricao_limpeza(df_original, df_limpo):
    descricao = "### Validação e Limpeza dos Dados\n\n"
    descricao += f"- **Total de linhas no CSV original**: {len(df_original)}\n"
    descricao += f"- **Total de linhas após remoção de duplicatas**: {len(df_limpo)} "
    descricao += f"(Removidas {len(df_original) - len(df_limpo)} duplicatas)\n"

    colunas_numericas = df_limpo.select_dtypes(
        include=['number']).columns.tolist()
    colunas_categoricas = df_limpo.select_dtypes(
        include=['object', 'category']).columns.tolist()
    descricao += f"- **Colunas numéricas**: {colunas_numericas}\n"
    descricao += f"- **Colunas categóricas**: {colunas_categoricas}\n"

    num_preenchidos_num = df_original[colunas_numericas].isnull(
    ).sum().sum() - df_limpo[colunas_numericas].isnull().sum().sum()
    num_preenchidos_cat = df_original[colunas_categoricas].isnull(
    ).sum().sum() - df_limpo[colunas_categoricas].isnull().sum().sum()
    descricao += f"- **Valores ausentes preenchidos nas colunas numéricas**: {num_preenchidos_num} (com a mediana)\n"
    descricao += f"- **Valores ausentes preenchidos nas colunas categóricas**: {num_preenchidos_cat} (com a moda)\n"
    colunas_removidas = [
        col for col in df_original.columns if col not in df_limpo.columns]
    if colunas_removidas:
        descricao += f"- **Colunas removidas**: {colunas_removidas}\n"
    else:
        descricao += f"- **Nenhuma coluna removida além das 'Unnamed: ...'**\n"

    return descricao

# Função para gerar Análise Exploratória de Dados (EDA)


def gerar_eda(df):
    eda = (
        "### Análise Exploratória de Dados (EDA)\n\n"
        f"- **Número total de linhas**: {len(df)}\n"
        f"- **Número total de colunas**: {len(df.columns)}\n"
        f"- **Tipos de dados**:\n"
    )
    for col in df.columns:
        eda += f"  - **{col}**: {df[col].dtype}\n"
    eda += "\n"
    eda += f"#### Estatísticas Descritivas:\n{df.describe(include='all')}\n"

    return eda

# Função para processar o CSV


def process_csv(file_path, batch_size=1000):
    try:
        # Ler o CSV com tratamento de erros específicos
        try:
            df_original = pd.read_csv(file_path)
        except FileNotFoundError:
            return "Erro: O arquivo não foi encontrado."
        except pd.errors.EmptyDataError:
            return "Erro: O arquivo CSV está vazio."
        except pd.errors.ParserError:
            return "Erro: Houve um problema ao analisar o arquivo CSV."

        # Validação e limpeza de dados
        df_limpo = validar_e_limpar_dados(df_original.copy())

        if len(df_limpo) == 0:
            return "O DataFrame está vazio após a limpeza. Verifique as etapas de limpeza e a qualidade dos dados."

        # Gerar descrição das etapas de limpeza
        descricao_limpeza = gerar_descricao_limpeza(df_original, df_limpo)

        # Gerar análise exploratória de dados (EDA)
        eda = gerar_eda(df_limpo)

        # Concatenar as descrições
        descricao_completa = descricao_limpeza + "\n\n" + eda

        # Tentar enviar todos os dados em um único lote
        try:
            sample_data = df_limpo.to_string(index=False)

            prompt = (
                "Você é um Analista de Dados altamente técnico, experiente e eficiente.Forneça uma análise técnica começando diretamente com os cabeçalhos markdown, sem introduções ou saudações."
                " Sua resposta deve ser em formato MARKDOWN, **bem organizada com títulos, subtítulos, listas (não use tabelas)**, e carregada de emojis relevantes para tornar a leitura mais dinâmica e informativa."
                " Sempre comece sua análise com uma visão geral dos dados fornecidos, onde a acurácia técnica é importante."
                " Inclua também uma seção detalhada sobre as etapas de validação e limpeza dos dados realizadas."
                " Explique detalhadamente as Estatísticas Descritivas (cada uma delas) de forma que qualquer usuario entenda."
                " Crie uma análise **bastante detalhada e perspicaz** dos dados abaixo, destacando as principais tendências, padrões e outliers que você encontrar."
                " Em sua análise, indique também detalhadamente, com base nos dados, quais melhores análises podem ser feitas: tais como descritivas, diagnósticas, preditivas e prescritivas."
                " Sugira **pelo menos 3 insights principais** que podem ser extraídos desses dados, explicando o significado de cada insight."
                " Para cada insight, considere qual **tipo de gráfico seria mais eficaz para visualizá-lo**. Responda sempre em PT-BR. Evite uso de imagens e links."
                "--- dito isso, \n\n"
                f"{descricao_completa}\n\n"
                f"---\n\n"
                f"{sample_data}"
            )

            model = genai.GenerativeModel(model_name="gemini-exp-1206")
            response = model.generate_content(prompt)
            analise_completa = response.text

            return analise_completa

        except AttributeError:
            return "Erro: Verifique se a biblioteca 'google.generativeai' está atualizada e se o atributo está correto."
        except Exception:
            # Determinar o número de lotes
            total_linhas = len(df_limpo)
            total_lotes = (total_linhas // batch_size) + \
                int(total_linhas % batch_size != 0)

            if total_lotes == 0:
                return "Nenhum lote para processar."

            try:
                model = genai.GenerativeModel(model_name="gemini-exp-1206")
            except AttributeError:
                return "Erro: Verifique se a biblioteca 'google.generativeai' está atualizada e se o atributo está correto."
            except Exception:
                return "Erro inesperado ao inicializar o modelo."

            respostas = []

            for i in tqdm(range(total_lotes), desc="Processando lotes"):
                start = i * batch_size
                end = start + batch_size
                lote = df_limpo.iloc[start:end]

                sample_data_lote = lote.to_string(index=False)

                prompt_lote = (
                    "Você é um Analista de Dados altamente técnico, experiente e eficiente.Forneça uma análise técnica começando diretamente com os cabeçalhos markdown, sem introduções ou saudações."
                    " Sua resposta deve ser em formato MARKDOWN, **bem organizada com títulos, subtítulos, listas (não use tabelas)**, e carregada de emojis relevantes para tornar a leitura mais dinâmica e informativa."
                    " Sempre comece sua análise com uma visão geral dos dados fornecidos, onde a acurácia técnica é importante."
                    " Inclua também uma seção detalhada sobre as etapas de validação e limpeza dos dados realizadas."
                    " Explique detalhadamente as Estatísticas Descritivas (cada uma delas) de forma que qualquer usuario entenda."
                    " Crie uma análise **bastante detalhada e perspicaz** dos dados abaixo, destacando as principais tendências, padrões e outliers que você encontrar."
                    " Em sua análise, indique também detalhadamente, com base nos dados, quais melhores análises podem ser feitas: tais como descritivas, diagnósticas, preditivas e prescritivas."
                    " Sugira **pelo menos 3 insights principais** que podem ser extraídos desses dados, explicando o significado de cada insight."
                    " Para cada insight, considere qual **tipo de gráfico seria mais eficaz para visualizá-lo**. Responda sempre em PT-BR. Evite uso de imagens e links."
                    "--- dito isso, \n\n"
                    f"{descricao_completa}\n\n"
                    f"---\n\n"
                    f"{sample_data_lote}"
                )

                try:
                    response_lote = model.generate_content(prompt_lote)
                    respostas.append(response_lote.text)
                except Exception:
                    continue

            analise_completa = "\n\n---\n\n".join(respostas)

            return analise_completa

    except Exception as e:
        return f"Erro ao processar o CSV: {str(e)}"
