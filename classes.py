from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy import insert, text, select

from sqlalchemy.orm import Session

from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, IntegerField, SubmitField, validators
from config import host, port, database, user, password

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=True, future=True)
metadata_obj = MetaData()

# create Table object via reflection from DB
build_table = Table("build", metadata_obj, autoload_with=engine)

height_list = ["Please select..."]
with Session(engine) as session:
    for row in session.execute(select(build_table.c.height)):
        height_list.append(row[0])

# Form classes
class IndexPageForm(FlaskForm):
    birthdate = DateField('Birthdate:', [validators.InputRequired()], format="%m/%d/%Y")
    gender = SelectField('Gender:', [validators.InputRequired()], choices=["Please select...", "Male", "Female"])
    height = SelectField('Height (in feet and inches):', [validators.InputRequired()], choices=height_list)
    weight = IntegerField('Weight (in pounds):', [validators.InputRequired(), validators.Length(min=1,max=3)])
    nicotine = SelectField('Nicotine use (Last 12 months):', [validators.InputRequired()], choices=[
        "Please select...", 
        "Yes", 
        "No", 
        "Other (vape, chewing tobacco, cigars, etc)"
        ])
    submit = SubmitField("Continue")