from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy import insert, text, select

from sqlalchemy.orm import Session

from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, IntegerField, SubmitField, BooleanField, validators
from config import host, port, database, user, password

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=False, future=True)
metadata_obj = MetaData()

# create Table objects via reflection from DB
build_table = Table("build", metadata_obj, autoload_with=engine)
cases_table = Table("cases", metadata_obj, autoload_with=engine)

# Populate list of form options from build DB
height_list = ["Please select..."]
with Session(engine) as session:
    for row in session.execute(select(build_table.c.height)):
        height_list.append(row[0])

dur_list = ["Less than 1 year ago", "1 - 2 years ago", "2 - 3 years ago", "3+ years ago"]

# Form classes
class IndexPageForm(FlaskForm):
    birthdate = DateField('Birthdate:', [validators.InputRequired()])
    gender = SelectField('Gender:', [validators.InputRequired()], choices=["Please select...", "Male", "Female"])
    height = SelectField('Height (in feet and inches):', [validators.InputRequired()], choices=height_list)
    weight = IntegerField('Weight (in pounds):', [validators.InputRequired()])
    nicotine = SelectField('Nicotine use (Last 12 months):', [validators.InputRequired()], choices=[
        "Please select...", 
        "Yes", 
        "No", 
        "Other (vape, chewing tobacco, cigars, etc)"
        ])
    submit = SubmitField("Continue")

class HealthHxForm(FlaskForm):
    heart_attack = BooleanField('Heart Attack? ')
    heart_attack_dur = SelectField('How many years ago?', choices=dur_list)
    stroke = BooleanField('Stroke? ')
    stroke_dur = SelectField('How many years ago?', choices=dur_list)
    tia = BooleanField('TIA / Mini-Stroke? ')
    tia_dur = SelectField('How many years ago?', choices=dur_list)
    cardio_surgery = BooleanField('Heart or circulatory surgery/procedure: ')
    cardio_surgery_dur = SelectField('How many years ago?', choices=dur_list)
    chf = BooleanField('Congestive Heart Failure? ')
    diabetes = BooleanField('Diabetes? ')
    insulin = BooleanField('Insulin use? ')
    complications = BooleanField('Complications of diabetes? ')
    insulin_dur = SelectField('Last used insulin? ', choices=dur_list)
    submit = SubmitField("Continue")