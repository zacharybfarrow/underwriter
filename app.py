from flask import Flask
from flask import render_template, request, redirect

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from config import host, port, database, user, password
from classes import build_table

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=True, future=True)

app = Flask(__name__)

# Get info from user to pass into underwriting db
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        # Populate height list from build table for drop-down menu
        height_list = []
        with Session(engine) as session:
            for row in session.execute(select(build_table.c.height)):
                height_list.append(row)
        return render_template("index.html", height_list=height_list)
    
    # if request is "POST" (meaning we have submitted the form)
    # save the information into a db Table called 'cases' and redirect to /health_profile

@app.route("/health_profile", methods=["POST"])
def health_profile():
    return render_template("health_profile")