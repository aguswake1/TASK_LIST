from decouple import config


class Config:  # configuraciones globales
    # definir llave secreta
    SECRET_KEY = 'holamundo'  # ModoSk3rE8080


class DevelopmentConfig(Config):  # config para entorno de desarrollo
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/TASK_LIST'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = "aolano@alumno.huergo.edu.ar"
    MAIL_PASSWORD = "crossfit1007"


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}  # dic almacena clases
