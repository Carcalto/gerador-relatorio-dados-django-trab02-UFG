# Sistema de Análise de Dados com IA 🤖📊

## Visão Geral 🌟

Este projeto é um sistema web avançado desenvolvido em Django que combina processamento de dados com Inteligência Artificial para gerar análises detalhadas a partir de arquivos CSV. O sistema utiliza a API do Google Gemini para enriquecer as análises com insights gerados por IA.

## Tecnologias Utilizadas 🛠️

- **Backend**: 
  - Django 5.1.5 🐍
  - Python 3.x 🐍
  - Pandas (Análise de Dados) 🐼
  - NumPy (Computação Numérica) 🔢
  - Google Gemini API (IA) 🤖

- **Frontend**:
  - HTML5/CSS3 🎨
  - JavaScript (ES6+) ⚡
  - Bootstrap 5 🎯
  - Font Awesome (Ícones) 🎭
  - Markdown Rendering 📝

## Funcionalidades Principais 💫

### 1. Processamento de Dados 📊
- Upload de arquivos CSV com validação de formato
- Limpeza automática de dados:
  - Remoção de duplicatas 🧹
  - Tratamento de valores nulos/ausentes 🔍
  - Identificação automática de tipos de dados 🏷️
- Processamento em lotes para arquivos grandes 📦

### 2. Análise Exploratória de Dados (EDA) 📈
- Estatísticas descritivas completas
- Detecção de outliers
- Análise de distribuição
- Correlações entre variáveis
- Identificação de padrões

### 3. Integração com IA 🧠
- Análise semântica dos dados via Google Gemini
- Geração de insights automáticos
- Sugestões de visualizações
- Interpretação contextual dos resultados

### 4. Interface do Usuário 🖥️
- Design responsivo e moderno
- Barra de progresso em tempo real
- Feedback visual interativo
- Renderização Markdown para relatórios
- Sidebar colapsável para melhor usabilidade

## Fluxo de Funcionamento 🔄

1. **Upload do Arquivo** 📤
   - Validação do formato CSV
   - Verificação inicial de integridade
   - Armazenamento temporário seguro

2. **Pré-processamento** 🔧
   ```python
   # Exemplo de limpeza de dados
   def validar_e_limpar_dados(df):
       # Remove duplicatas
       df = df.drop_duplicates()
       # Trata valores nulos
       df_numerico = df.select_dtypes(include=['float64', 'int64'])
       df[df_numerico.columns] = df_numerico.fillna(df_numerico.median())
       return df
   ```

3. **Análise Exploratória** 🔍
   - Geração de estatísticas descritivas
   - Identificação de correlações
   - Análise de distribuições

4. **Processamento com IA** 🤖
   - Envio dos dados processados para API Gemini
   - Geração de insights contextualizados
   - Sugestões de visualizações

5. **Geração do Relatório** 📑
   - Formatação em Markdown
   - Inclusão de emojis para melhor legibilidade
   - Estruturação hierárquica das informações

## Segurança e Performance 🛡️

- **Segurança**:
  - Validação de arquivos
  - Proteção CSRF
  - Limpeza automática de arquivos temporários
  - Sanitização de dados

- **Performance**:
  - Processamento assíncrono
  - Otimização de memória
  - Processamento em lotes
  - Cache de resultados

## Requisitos do Sistema 📋

```txt
Django==5.1.5
pandas==2.2.3
numpy==2.2.2
google-generativeai==0.8.4
python-decouple==3.8
markdown==3.7
```

## Instalação e Configuração 🚀

1. **Clone o repositório**:
   ```bash
   git clone [url-do-repositorio]
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   - Crie um arquivo `.env`
   - Adicione sua chave API do Google Gemini
   - Configure outras variáveis necessárias

5. **Execute as migrações**:
   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor**:
   ```bash
   python manage.py runserver
   ```

## Uso do Sistema 📱

1. Acesse a interface web
2. Faça upload do arquivo CSV
3. Aguarde o processamento (barra de progresso)
4. Visualize o relatório gerado
5. Explore os insights e análises

## Boas Práticas de Uso 📌

- Use arquivos CSV bem formatados
- Prefira conjuntos de dados limpos
- Aguarde o processamento completo
- Verifique os requisitos de formato

## Contribuição 🤝

Contribuições são bem-vindas! Para contribuir:
1. Faça um Fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença 📄

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Autor 👨‍💻

**CELIO OLIVEIRA CARCALTO**
- Matrícula: 2024201158
- Universidade Federal de Goiás
- Especialização em Sistemas e Agentes Inteligentes

## Suporte 💬

Para suporte e dúvidas:
- Abra uma issue
- Entre em contato via email
- Consulte a documentação

## Acesso ao Sistema 🌐

### Acesso Local 🏠
Para acessar o sistema localmente:
```bash
python manage.py runserver
```
Acesse: http://localhost:8000

### Acesso Externo 🌍
Para permitir que outros computadores na rede acessem o sistema:

1. **Descubra seu IP local**:
   ```bash
   # Windows
   ipconfig
   
   # Linux/Mac
   ifconfig
   ```

2. **Inicie o servidor com seu IP**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. **Acesso**:
   - Outros usuários na mesma rede podem acessar usando:
   ```
   http://seu_ip:8000
   ```
   - Exemplo: `http://192.168.1.100:8000`

4. **Acesso Externo à Rede Local**:
   - Configure o redirecionamento de porta no seu roteador (port forwarding)
   - Libere a porta 8000 no firewall
   - Use seu IP público para acesso externo
   - Considere usar serviços como ngrok para acesso temporário seguro:
     ```bash
     # Instale o ngrok e execute:
     ngrok http 8000
     ```

⚠️ **Notas de Segurança**:
- Em ambiente de produção, configure ALLOWED_HOSTS apropriadamente
- Use HTTPS para conexões externas
- Mantenha o sistema e dependências atualizados
- Considere implementar autenticação de usuários
- Monitore os logs de acesso

## Configuração do Ngrok para Acesso Externo 🔗

O ngrok permite que seu sistema seja acessível publicamente de forma segura, sem necessidade de configurar roteador ou firewall.

### Instalação do Ngrok 📥

1. **Windows**:
   ```bash
   # Via Chocolatey
   choco install ngrok

   # OU baixe o executável em https://ngrok.com/download
   # Extraia o arquivo ngrok.exe para uma pasta de sua preferência
   ```

2. **Linux**:
   ```bash
   # Via Snap
   sudo snap install ngrok

   # OU via apt (Ubuntu/Debian)
   curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
   ```

3. **macOS**:
   ```bash
   # Via Homebrew
   brew install ngrok
   ```

### Configuração do Ngrok 🔧

1. **Crie uma conta gratuita**:
   - Acesse [https://ngrok.com](https://ngrok.com)
   - Faça o registro
   - Copie seu authtoken

2. **Configure o authtoken**:
   ```bash
   ngrok config add-authtoken seu_token_aqui
   ```

### Usando o Ngrok com o Sistema 🚀

1. **Inicie o servidor Django**:
   ```bash
   python manage.py runserver
   ```

2. **Em outro terminal, inicie o ngrok**:
   ```bash
   ngrok http 8000
   ```

3. **Acesso**:
   - O ngrok fornecerá URLs como:
     ```
     https://seu-codigo-unico.ngrok.io
     ```
   - Compartilhe esta URL para acesso externo
   - A URL é válida enquanto o ngrok estiver rodando

### Recursos do Ngrok ⚙️
- Interface web de inspeção: `http://localhost:4040`
- Visualização de todo tráfego HTTP
- Replay de requisições
- Inspeção de WebSockets
- Proteção por senha (planos pagos)

### Limitações da Versão Gratuita 📝
- Sessões expiram em 2 horas
- Subdomínios aleatórios
- 1 túnel por vez
- Largura de banda limitada

⚠️ **Dicas de Segurança**:
- Não deixe o ngrok rodando indefinidamente
- Use apenas durante desenvolvimento/demonstração
- Monitore o tráfego pela interface de inspeção
- Considere planos pagos para uso comercial

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub! 