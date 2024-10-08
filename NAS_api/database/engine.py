from pathlib import Path

from sqlalchemy import create_engine

from .similarity_search import VectorDB

base_path = Path(__file__).resolve().parent

url = f'sqlite:////{base_path}/sqlite_data.db'
db_engine = create_engine(url)

vectordb_engine = VectorDB(path=base_path)
