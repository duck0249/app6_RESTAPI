## App6 : REST API, Create REST API powered by Flask
from flask import Flask, render_template
# import requests
import pandas as pd
from datetime import datetime

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
        filename = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
        df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

        date = datetime.strptime(date, "%Y%m%d")
        date = date.strftime("%Y-%m-%d")

        temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
        return {"station": station,
        		"date": date,
        		"temperature": temperature}

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
