from flaskblue import app

@app.route('/')
def home():
    return '<h1>Hello world!</h1>'

@app.route('/about')
def about():
    return 'About Me'
