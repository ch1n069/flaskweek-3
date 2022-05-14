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

    SQLALCHEMY_DATABASE_URI = 'postgres://omdvhqdqcoeccr:fbc1f313c03451df38657d28b84021eeec857faef671de48b53c3c00ec3faf63@ec2-52-4-104-184.compute-1.amazonaws.com:5432/d6nrk5ftf2lv0v'
    
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
