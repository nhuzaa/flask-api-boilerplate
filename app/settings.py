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

WEATHER_APP_BASE_URL = "https://samples.openweathermap.org/data/2.5"
WEATHER_APP_ID = "b6907d289e10d714a6e88b30761fae22"
