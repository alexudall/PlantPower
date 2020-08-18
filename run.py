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

'''
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
    
@app.route('/results')
def results():
    return render_template('results.html')
'''