from flask import Flask, render_template, redirect, url_for 

app = Flask(__name__) 


@app.route("/") 
def layout(): 
	return render_template("layout.html") 

@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/query")
def query_analysis():
	return render_template("query_analysis.html")

@app.route("/pawn")
def pawn():
	return render_template("pawned.html")

@app.route("/webarchive")
def webarchive():
	return render_template("web_archive.html")

if __name__ == "__main__": 
	app.run(debug=True, port=8001) 