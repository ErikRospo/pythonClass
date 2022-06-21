from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return '''<!DOCTYPE html>
            <html lang="en">
                <head>
                    <title>Document</title>
                </head>
                <body>
                <p> hello </p>
                <div>
                <a href="/about">About</a><br>
                <a href="/test">Test</a><br>
                <a href="/test2">Test 2</a><br>
                </div>
                
                </body>
            </html>'''
    # return "<h1>Hello, World!</h1>"
    
@app.route('/about')
def about():
    return "About"

@app.route('/test')
def test():
    user={'username':'Erik'}
    return render_template('test.html', user=user)
@app.route('/test2')
def test2():
    user = {'username': 'Erik'}
    sample_data = [
    {
    'author': {'username': 'ER'},
    'body': 'Hello!'
    },
    {
    'author': {'username': 'ERIK'},
    'body': 'Welcome to Flask!'
    }
    ]
    return render_template('test2.html', user=user, sample_data=sample_data)
