from pathlib import Path

from sqlalchemy import create_engine

print(Path())
engine = create_engine('sqlite:///')
