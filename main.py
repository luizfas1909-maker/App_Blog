from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

username = 'postgres'
password = '123456'
host = 'localhost'
port = 5432
database = 'blog'
DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
