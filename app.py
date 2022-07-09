from flask import Flask
from flask import render_template, request, redirect, url_for

from sqlalchemy import create_engine

from config import host, port, database, user, password, secret_key
from classes import IndexPageForm
from helpers import store_case_data

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str, echo=True, future=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

# Get info from user to pass into underwriting db
@app.route("/", methods=["GET", "POST"])
def index():
    form = IndexPageForm()
    if form.validate_on_submit():
        print("validated")
        # Store user input in db
        case = store_case_data(form)
        # Send case data along with redirect
        return redirect(url_for("health_hx", case=case))

    # Institute some sort of error flashing
    else:
        print("did not validate")
        print(form.birthdate)
        print(form.errors)
        return render_template("index.html", form=form)

@app.route("/health_hx", methods=["GET", "POST"])
def health_hx():
    return render_template("health_hx.html", case=request.args.get("case"))