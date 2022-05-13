import os 




class Config:
    '''
    General configuration parent class
    '''
    

    # SQLALCHEMY_DATABASE_URI = 'postgres://sijcttxzgupmue:6320dfd827ee78689b697ac2d2416277d620fbb88ba3c335b2e9d0a4e533b09e@ec2-107-22-238-112.compute-1.amazonaws.com:5432/dcsav0n275511b'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True






class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''


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