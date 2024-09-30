from pathlib import Path

from sqlalchemy import create_engine

base_path = Path(__file__).resolve().parent

url = f'sqlite:////{base_path}/sqlite.db'
db_engine = create_engine(url)
