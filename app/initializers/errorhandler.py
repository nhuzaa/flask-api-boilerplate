from flask import jsonify, current_app
from werkzeug.exceptions import HTTPException
from marshmallow import exceptions as marsh_exceptions
from werkzeug import exceptions as werkzeug_exceptions

from raven.contrib.flask import Sentry


def handle_404(e):
    return jsonify(error="Resource not found"), 404


def handle_marsh_validation_error(e):
    return jsonify(error=e.messages), 422


def handle_global_error(app, sentry):
    def _(e):
        code = 500
        message = "Something went wrong"

        if isinstance(e, HTTPException):
            code = e.code
            message = str(e)

        if code == 500:
            current_app.logger.error(e)

        if app.debug:
            raise e

        sentry.captureException()

        return jsonify(error=message), code

    return _


def init_errorhandler(app):
    sentry = Sentry(dsn=app.config["SENTRY_DSN"])
    sentry.init_app(app)

    app.register_error_handler(werkzeug_exceptions.NotFound, handle_404)
    app.register_error_handler(
        marsh_exceptions.ValidationError, handle_marsh_validation_error
    )
    app.register_error_handler(Exception, handle_global_error(app, sentry))
