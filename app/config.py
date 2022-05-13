import os 




class Config:
    '''
    General configuration parent class
    '''
    

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:newpassword@localhost/pitch'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("brunolalpachino@gmail.com")
    MAIL_PASSWORD = os.environ.get("Elh4g9yq")



config_options = {
'development':DevConfig,
'production':ProdConfig
}