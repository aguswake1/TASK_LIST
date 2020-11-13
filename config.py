class Config:  # configuraciones globales
    # definir llave secreta
    SECRET_KEY = 'holamundo'  # ModoSk3rE8080


class DevelopmentConfig(Config):  # config para entorno de desarrollo
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/TASK_LIST'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}  # dic almacena clases
