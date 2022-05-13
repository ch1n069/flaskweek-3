from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail









bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
mail = Mail()

bcrypt = Bcrypt()






def create_app(config_name): 


    app = Flask(__name__)
    # Creating the app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:newpassword@localhost/pitchpostgres://sijcttxzgupmue:6320dfd827ee78689b697ac2d2416277d620fbb88ba3c335b2e9d0a4e533b09e@ec2-107-22-238-112.compute-1.amazonaws.com:5432/dcsav0n275511b'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'any secret string'

    
    app.config.from_object(config_options[config_name])





    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)






    # Will add the views and formss
    #registering a blueprint
    from app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    # from app.auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix='/authenticate')



    
    #SETTING UP CONFIGURATION
    # from .request import configure_request
    # configure_request(app)
    
   
    return app
        