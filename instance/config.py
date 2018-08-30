class BaseConfig(object):
    """parent configuration class"""
    DEBUG = True
    DB = 'stack_db'

class DevelopmentConfig(BaseConfig):
    """Configurations for Development."""
    DEBUG=True
    DB ='stack_db'

class TestingConfig(BaseConfig):
    """Configurations for Testing."""
    Debug =False
    TESTING = True
    DB = 'test_db'

class ProductionConfig(BaseConfig):
    """Configurations for Production."""
    DEBUG =False

    

app_config ={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

