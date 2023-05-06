
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key",
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
