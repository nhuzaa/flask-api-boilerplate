import os


def init_config(app, is_test):
    app.config.from_object("app.settings")

    try:
        if is_test:
            app.config["TESTING"] = True
            app.config.from_pyfile("test_config.py")
        else:
            app.config.from_pyfile("config.py")
    except FileNotFoundError:
        configs = ["SQLALCHEMY_DATABASE_URI"]
        for config in configs:
            app.config[config] = os.environ[config]
