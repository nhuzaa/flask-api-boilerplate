from flask import jsonify
from werkzeug.exceptions import HTTPException
from marshmallow import exceptions as marsh_exceptions


def init_errorhandler(app):
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
        return jsonify(error=message), code
