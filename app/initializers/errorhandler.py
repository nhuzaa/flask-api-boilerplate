from flask import jsonify, current_app
from werkzeug.exceptions import HTTPException
from marshmallow import exceptions as marsh_exceptions
from werkzeug import exceptions as werkzeug_exceptions


def init_errorhandler(app):
    @app.errorhandler(werkzeug_exceptions.NotFound)
    def handle_404(e):
        return jsonify(error="Resource not found"), 404

    @app.errorhandler(marsh_exceptions.ValidationError)
    def handle_marsh_validation_error(e):
        return jsonify(error=e.messages), 422

    @app.errorhandler(Exception)
    def handle_global_error(e):
        code = 500
        message = "Something went wrong"

        if isinstance(e, HTTPException):
            code = e.code
            message = str(e)

        if code == 500:
            current_app.logger.error(e)

        if app.debug:
            raise e

        return jsonify(error=message), code
