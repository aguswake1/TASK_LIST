class Config:  # configuraciones globales
    # definir llave secreta
    SECRET_KEY = 'holamundo'  # ModoSk3rE8080


class DevelopmentConfig(Config):  # config para entorno de desarrollo
    DEBUG = True
    SQLACHEMY_DATABASE_URI = 'mysql://root:root@localhost/TASKLIST'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}  # dic almacena clases
