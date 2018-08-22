# DEFAULT CONFIGURATIONS

import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://sudhirt4@localhost:5432/testing"

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = 'logs/app.log'
LOGGING_LEVEL = logging.DEBUG
