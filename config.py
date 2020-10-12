class Config:  # configuraciones globales
    pass


class DevelopmentConfig(Config):  # config para entorno de desarrollo
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}  # dic almacena clases
