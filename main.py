import os
from flask import Flask, render_template, flash, request, redirect, url_for
from bs4 import BeautifulSoup
from src.parse_bday import parse_bday

# Flask instance; allows for instance (database) outside folder
app = Flask(__name__, instance_relative_config=True)

app.secret_key = os.urandom(12)

@app.route('/', methods = ['GET', 'POST'])
def index():

	return render_template("index.html", )

@app.route('/parse-bday-data', methods=['GET', 'POST'])
def parse_bday_data():
    return parse_bday(request.get_json())

if __name__ == "__main__":
    app.run()