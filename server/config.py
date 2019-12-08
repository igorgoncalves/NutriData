class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY="\xbde\x1c\xc6\xccA\xc7\xe39\xc1\x90\xff\x8a\xb8B\x16\xaf\xc1\x14&%$\x954"

class ProductionConfig(Config):
    DEBUG = True
    DATABASE_NAME = 'dbNutridata'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_NAME = 'dbNutridata'