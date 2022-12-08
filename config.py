class Config:
    DEBUG = True
    TESTING =True

    # config base de  datos
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://noroot:noroot@localhost:3306/test"

class ProductionConfig(Config):
    DEBUG=False

class DevelopmentConfig(Config):
    SECRET_KEY = "dev"