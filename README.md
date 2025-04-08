# 📚 Web Scraping de Livros com Armazenamento em Banco de Dados

Este projeto realiza **web scraping** de dados de livros a partir de uma fonte online, armazena os dados em um arquivo CSV e também em um banco de dados SQLite. Além disso, conta com uma interface web para visualização dos livros.

---

## 🧱 Estrutura do Projeto

```
WEB_SCRAPING_BOOKS/
├── app/
│   ├── db/
│   │   ├── connection.py         # Conexão com o banco de dados
│   │   └── database.py           # Funções para manipulação do banco
│   ├── routes/
│   │   ├── __init__.py           # Inicialização de rotas Flask
│   │   ├── books.py              # Rota para exibir os livros
│   │   └── scraper.py            # Rota para iniciar o scraping
│   ├── scraper/
│   │   └── book_scraping.py      # Lógica de scraping
│   └── templates/
│       ├── base.html             # Template base
│       └── index.html            # Página inicial com listagem dos livros
├── data/
│   └── save_books.csv            # Exportação dos livros para CSV
├── database/
│   └── BookingDB.db              # Banco de dados SQLite
├── .gitignore
├── README.md                     # Este arquivo
├── requirements.txt              # Dependências do projeto
├── run_scraper.py                # Executa o scraping diretamente
├── run.py                        # Inicia o servidor Flask
└── text/                         # (pasta opcional para armazenar textos brutos)
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Enockjoao/WebScraping_Books.git
cd web_scraping_books
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate     # Linux/MacOS
.venv\Scripts\activate        # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🖥️ Como usar

### Executar o scraper manualmente:

```bash
python run_scraper.py
```

### Iniciar o servidor web:

```bash
python run.py
```

Acesse em [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Funcionalidades

- 🔍 Scraping automatizado de dados de livros (título, preço, disponibilidade, etc.)
- 🧾 Armazenamento em arquivo CSV e banco de dados SQLite
- 🌐 Interface web com Flask para visualização dos livros
- 🔄 Reprocessamento dos dados a partir da rota `/scrape`

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Flask
- BeautifulSoup
- Requests
- SQLite
- HTML (Jinja2 Templates)

---

## 📂 Organização dos Módulos

| Módulo         | Descrição |
|----------------|-----------|
| `app/db`       | Conexão e manipulação do banco de dados SQLite |
| `app/routes`   | Lógica das rotas da aplicação Flask |
| `app/scraper`  | Funções de scraping com BeautifulSoup |
| `templates`    | Interface HTML da aplicação |
| `data/`        | Armazenamento dos dados exportados |
| `database/`    | Banco de dados persistente SQLite |

---

## ✅ Checklist

- [x] Estrutura modular
- [x] Interface web com Flask
- [x] Banco de dados integrado
- [x] Exportação para CSV
- [x] Documentação clara

---

## 📌 To-do Futuro

- Adicionar testes automatizados (Pytest)
- Paginação e filtros na interface web
- Integração com banco de dados PostgreSQL
- Deploy na nuvem (Render, Heroku, etc.)

---

## 🧑‍💻 Autor

**Enock** – [GitHub](https://github.com/Enockjoao)
