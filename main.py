## App6 : REST API, Create REST API powered by Flask
from flask import Flask, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)
df_station = pd.read_csv("./data_small/stations.txt", skiprows=17)
df_station = df_station.iloc[:20,[0,1]]
df_html = df_station.to_html(header=True)


@app.route("/")
def home():
    try:
        return render_template("home.html", table=df_html)
    except Exception as e:
        return f"Error: {e}"


@app.route("/api/v1/<station>/<date>")
def api_all(station, date):
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


@app.route("/api/v1/<station>/")
def api_station(station):
	try:
		filename = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
		df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
		result = df.to_dict(orient="records")

		return result

	except Exception as e:
		return f"Error: {e}"


@app.route("/api/v1/yearly/<station>/<year>")
def api_yearly(station, year):
	try:
		filename = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
		df = pd.read_csv(filename, skiprows=20)
		df["    DATE"] = df["    DATE"].astype(str)
		result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")

		return result
	
	except Exception as e:
		return f"Error : {e}"

if __name__ == "__main__":
    app.run(debug=True)
