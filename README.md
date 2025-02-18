# TGBackup

**TGBackup** é uma ferramenta de backup que utiliza o Telegram para armazenar arquivos e diretórios de forma segura e prática. Utilizando a biblioteca [Telethon](https://github.com/LonamiWebs/Telethon), a aplicação realiza upload, download e gerenciamento de arquivos, dividindo arquivos grandes em "chunks" para contornar as limitações de tamanho do Telegram.

---

## Recursos

- **Upload de Arquivos e Diretórios:** Divisão de arquivos em "chunks" (partes) para upload via Telegram.
- **Download:** Recuperação dos arquivos/diretórios armazenados, com reagrupamento dos "chunks".
- **Gerenciamento:** Listagem e remoção de arquivos/diretórios através de comandos.
- **Banco de Dados SQLite:** Armazena metadados dos arquivos enviados para facilitar a busca e o gerenciamento.
- **Interface via Linha de Comando:** Simples e intuitiva para operações de backup.
- **Logs Verbosos (opcional):** Ative para obter mensagens detalhadas de depuração.

---

## Visão Geral

TGBackup permite que você faça backup dos seus arquivos enviando-os para a sua conta do Telegram. A aplicação lê um arquivo de configuração (`config.json`) contendo as credenciais da API do Telegram, o número de telefone, o caminho para o banco de dados e outras configurações. Após o upload, os metadados do arquivo são armazenados em um banco de dados SQLite, possibilitando a recuperação e a gestão dos arquivos posteriormente.

---

## Estrutura do Projeto

```markdown
TGBackup/
│
├── src/
│   ├── config.py         # Leitura e gerenciamento das configurações
│   ├── db.py             # Manipulação do banco de dados SQLite
│   ├── files.py          # Funções para divisão de arquivos em chunks e formatação de tamanho
│   ├── main.py           # Ponto de entrada da aplicação
│   └── telegram.py       # Integração com o Telegram (upload/download/gerenciamento)
│
├── .gitignore            # Arquivos e pastas a serem ignorados pelo Git
├── README.md             # Este arquivo de documentação
├── example.config.json   # Exemplo de arquivo de configuração
├── requirements.txt      # Dependências do projeto
├── run.bat               # Script para execução no Windows
└── run.sh                # Script para execução em sistemas tipo Unix
```



## Requisitos

- **Python 3.6+**
- **Dependências:**
  - Telethon
  - termcolor
  - prettytable
  - tqdm
  - sqlite3 (geralmente incluso na instalação padrão do Python)
- **Conta no Telegram:** Para obter `api_id` e `api_hash`.


## Instalação

1. **Clone o repositório:**

    ```sh
    git clone https://github.com/hugo-furtaddo/TGBackup.git
    cd TGBackup
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```sh
    pip install -r requirements.txt
    ```


## Configuração

1. **Crie o arquivo de configuração:**

    Copie o arquivo `example.config.json` para `config.json` na raiz do projeto e preencha com os dados corretos:

    ```json
    {
      "telegram_api_id": "SEU_API_ID",
      "telegram_api_hash": "SEU_API_HASH",
      "phone_number": "SEU_NUMERO_DE_TELEFONE",
      "db_file": "telesync.db",
      "verbose": false
    }
    ```

2. **Ajuste as configurações conforme necessário:**
    - **verbose:** Defina como `true` para obter logs detalhados.
    - **db_file:** Caminho/nome do arquivo de banco de dados SQLite.

## Uso

A aplicação é operada via linha de comando a partir do script `main.py`. Abaixo estão os comandos suportados:

### Upload de Arquivos


    python src/main.py upload <caminho_do_arquivo>


- O arquivo será dividido em chunks (caso ultrapasse o limite do Telegram) e enviado para a sua conta.

### Upload de Diretórios


    python src/main.py upload <caminho_do_diretorio>

- Caso o caminho seja de um diretório, todos os arquivos contidos nele serão enviados.

### Download

    python src/main.py download <identificador_ou_nome_do_arquivo>


- Realiza a busca do arquivo no banco de dados e efetua o download dos chunks, reunindo-os no arquivo original.

### Listar Arquivos

    python src/main.py list


- Lista todos os arquivos e diretórios presentes no banco de dados, exibindo ID, nome, caminho, tamanho, quantidade de chunks, tipo e data de envio.

### Remover Arquivos


    python src/main.py remove <identificador_ou_nome_do_arquivo>


- Remove o arquivo (ou diretório) do banco de dados e das mensagens enviadas pelo Telegram.

## Scripts de Execução

Para facilitar a execução em diferentes sistemas operacionais, estão disponíveis:

- **Windows:**
  
  ```sh
  run.bat upload <caminho_do_arquivo_ou_diretorio>
  ```

- **Linux/Mac:**
  
  ```sh
  ./run.sh upload <caminho_do_arquivo_ou_diretorio>
  ```

Ambos os scripts ativam o ambiente virtual (se existir) e executam o `main.py`.
