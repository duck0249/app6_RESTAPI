## App6 : REST API, Create REST API powered by Flask
from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    try:
        return render_template("home.html")
    except Exception as e:
        return f"Error: {e}"


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    try:
        # df = pandas.read_csv("")
        temperature = 23
        return {"station": station,
        		"date": date,
        		"temperature": temperature}

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
