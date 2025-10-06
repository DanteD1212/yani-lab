import os

class Config:
    """Configuración base para la aplicación."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuración para producción."""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'production-secret-key-must-be-set'

class TestingConfig(Config):
    """Configuración para pruebas."""
    TESTING = True
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}