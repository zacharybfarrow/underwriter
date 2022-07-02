from sqlalchemy import insert, select, create_engine
from sqlalchemy.orm import Session

from config import user, password, host, database

from classes import cases_table

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=True, future=True)

def store_case_data(form):
    with Session(engine) as session:
        insert_stmt = insert(cases_table).values(
            birthdate=form.birthdate.data,
            gender=form.gender.data,
            height=form.height.data,
            weight=form.weight.data,
            nicotine=form.nicotine.data).returning(
            cases_table.c.birthdate,
            cases_table.c.gender,
            cases_table.c.height,
            cases_table.c.weight,
            cases_table.c.nicotine
        )
        print("executing query")
        result = session.execute(insert_stmt)
        session.commit()
        return result