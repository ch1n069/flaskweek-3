from distutils.debug import DEBUG
import os 




class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = '2345678uytrsghgsfaetyrjhsvsfZGv'
    

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:newpassword@localhost/pitch'


#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("brunolalpachino@gmail.com")
    MAIL_PASSWORD = os.environ.get("Elh4g9yq")






class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = ' postgres://lywzpbzlgcsixz:ff0d78e94cdb6245ee2025211ef7542df5df06c95fd0426cb02e901e49f29719@ec2-54-172-175-251'
    
    DEBUG = False



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings

    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:newpassword@localhost/pitch'


    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}

    # # app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://moringa:newpassword@localhost/watchlist'
