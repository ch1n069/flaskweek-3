from flask import render_template,redirect,url_for,abort
from app import app





#views

@app.route('/')
def index():

    '''The home page of the application'''



    return render_template('index.html')
    