from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
MENUDB = 'plants.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next_page')
def next_page():
    return render_template('next_page.html')

    
@app.route('/results', methods=['POST'])
def results():
    sun = request.form["sun"]
    indoor = request.form["indoor"]
    water = request.form["water"]
    plants = []
    con = sqlite3.connect(MENUDB)
    cur = con.execute('SELECT * FROM plants WHERE sun=? AND indoor=? AND water=?', (sun, indoor, water))
    for row in cur:
        plants.append(list(row))
    con.close()
    
    

    return render_template('results.html',plants=plants, indoor=indoor)

