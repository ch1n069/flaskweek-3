from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import DevConfig




app = Flask(__name__,instance_relative_config = True)



# starting configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
app.config['SECRET_KEY'] = 'any secret string'





from app import views