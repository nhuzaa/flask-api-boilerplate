from logging.handlers import TimedRotatingFileHandler
import logging


def init_logging(app):
    # Configure logging
    handler = TimedRotatingFileHandler('logs/app.log', when='midnight', interval=1, backupCount=10)
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

    app.logger.addHandler(handler)
