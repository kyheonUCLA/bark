from flask import render_template, redirect, url_for
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ky')
def ky():
    return render_template('base.html')

@app.route('/themes')
def themes():
    return render_template('themes.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')