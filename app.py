from flask import Flask
from flask import render_template, request, redirect, url_for

from sqlalchemy import create_engine

from config import host, port, database, user, password, secret_key
from classes import HealthHxForm, IndexPageForm
from helpers import store_case_data

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=True, future=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

# Get info from user to pass into underwriting db
@app.route("/", methods=["GET", "POST"])
def index():
    form = IndexPageForm()
    # If form is being submitted
    if request.method == "POST":
        if form.validate_on_submit():
            print("validated")
            # Store user input in db
            case = store_case_data(form)
            # Send case data along with redirect
            return redirect(url_for("health_hx", case=case))

        # If form wasn't validated, handle errors
        elif not form.validate_on_submit():
            print(form.errors)
            return render_template("index.html", form=form)
        
        # Accessing form from GET request
    if request.method == "GET":
        return render_template("index.html", form=form)

@app.route("/health_hx", methods=["GET", "POST"])
def health_hx():
    form = HealthHxForm()

    # If form is being submitted
    if request.method == "POST":
        # Check for form validation
        if form.validate_on_submit():
            print("health_hx validated")
            return redirect(url_for("rx"))
            # Store user input in db
        
        return render_template("health_hx.html", form=form)

    # If accessing from redirect
    if request.method == "GET":
        return render_template("health_hx.html", form=form)

@app.route("/rx", methods=["GET", "POST"])
def rx():
    if request.method == "POST":
        # submit the medications
        return render_template("rx.html")
    
    if request.method == "GET":
        return render_template("rx.html")