from flask import Flask
from flask import render_template, request, redirect

from sqlalchemy import create_engine

from config import host, port, database, user, password, secret_key
from classes import build_table, IndexPageForm

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=True, future=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

# Get info from user to pass into underwriting db
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        form = IndexPageForm()
        return render_template("index.html", form=form)
    
    # if request is "POST" (meaning we have submitted the form)
    # validate and save the information into a db Table called 'cases' and redirect to /health_profile

@app.route("/health_profile", methods=["POST"])
def health_profile():
    return render_template("health_profile")