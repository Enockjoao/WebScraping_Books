import os
from sqlalchemy import create_engine

# Obter o caminho absoluto para o diretório do banco de dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_DIR = os.path.join(BASE_DIR, 'database')
DB_PATH = os.path.join(DB_DIR, '../database/BookingDB.db')

# Criar diretório do banco de dados se não existir
os.makedirs(DB_DIR, exist_ok=True)

# Criar engine com caminho absoluto
engine = create_engine(f'sqlite:///{DB_PATH}')