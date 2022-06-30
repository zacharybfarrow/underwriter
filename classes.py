from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy import insert, text
from config import host, port, database, user, password

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=True, future=True)
metadata_obj = MetaData()

# create Table object via reflection from DB
build_table = Table("build", metadata_obj, autoload_with=engine)