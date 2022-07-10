from sqlalchemy import insert, select, create_engine
from sqlalchemy.orm import Session

from config import user, password, host, database

from classes import cases_table

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=False, future=True)

def store_case_basics(form):
    """Takes user input from the IndexPageForm and stores in DB, generating unique id for the current case.
    Result is a CursorResult object that holds a row with all the inserted data.
    Returns the newly created case_id to be stored in the session data."""

    with Session(engine) as session:
        insert_stmt = insert(cases_table).values(
            birthdate=form.birthdate.data,
            gender=form.gender.data,
            height=form.height.data,
            weight=form.weight.data,
            nicotine=form.nicotine.data).returning(
            cases_table.c.case_id,
            cases_table.c.birthdate,
            cases_table.c.gender,
            cases_table.c.height,
            cases_table.c.weight,
            cases_table.c.nicotine
        )
        print("executing query")
        result = session.execute(insert_stmt)   # this is returning a CursorResult object (memory location), not raw table data
        case_id = 0                             # declaring variable to store case_id
        for row in result:
            case_id = row._mapping["case_id"]   # row._mapping gives you a dict of column names and row data
        session.commit()
        return case_id           

def store_case_dx(form, case_id):
    with Session(engine) as session:
        # update dx column of cases db for our case id
        # check to see if value of column is null (as in no diagnoses currently in db)
        # if so, use insert statement
        
        # if value not null,
        # use array_append - will need sqlalchemy text method I think
        return
