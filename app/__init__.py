from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate








bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()






def create_app(config_name): 


    app = Flask(__name__)
    # Creating the app configurations
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:newpassword@localhost/pitch'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'any secret string'

    
    app.config.from_object(config_options[config_name])





    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)





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
        