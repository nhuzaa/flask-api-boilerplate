from app.initializers import errorhandler, loghandler, confighandler


def setup_initializers(app, is_test):
    confighandler.init_config(app, is_test)
    errorhandler.init_errorhandler(app)
    if not is_test:
        loghandler.init_logging(app)
