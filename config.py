from os import urandom
from os import environ


class Config(object):
	DEBUG = False
	TESTING = False
	PYTHONUNBUFFERED = 1
	API_DB_CONN_STR = environ['API_DB_CONN_STR']
	API_WEAPONS_DB_CONN_STR = environ['API_WEAPONS_DB_CONN_STR']
	THREAT_INTEL_LIST_BUCKET = environ['THREAT_INTEL_DATASET_BUCKET']
	THREAT_INTEL_LIST_FORMATS_BUCKET = environ['THREAT_INTEL_LIST_FORMATS_BUCKET']
	THREAT_INTEL_LIST_BLACKLIST = ('scan-dangerous_amplifiers', 'scan-uashieldtargets')
	AUDIT_LOG_SERVER = environ['AUDIT_LOG_SERVER']
	LOG_SERVER = environ['LOG_SERVER']
	REDIRECT_TO_HTTPS = environ.get("REDIRECT_TO_HTTPS")


class ProductionConfig(Config):
	SECRET_KEY = urandom(16) 


class DevelopmentConfig(Config):
	DEBUG = True
	SECRET_KEY = "dev"


class TestingConfig(Config):
	# TODO: This will be taken care during setting up of testing framework.
	TESTING = True
	DEBUG = True
	API_DB_CONN_STR = ""
	API_WEAPONS_DB_CONN_STR = ""
	THREAT_INTEL_LIST_BUCKET = ""
	THREAT_INTEL_LIST_FORMATS_BUCKET = ""
	AUDIT_LOG_SERVER = ""
	LOG_SERVER = ""