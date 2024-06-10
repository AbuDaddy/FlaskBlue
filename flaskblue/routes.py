from flaskblue import app
from flask import render_template

@app.route('/')
def home():
    return render_template('layout.html', title='Home')

@app.route('/about')
def about():
    return 'About Me'
