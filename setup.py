from setuptools import setup, find_packages

setup(
    name="app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "psycopg2-binary",
        "Flask==1.0.2",
        "flask-sqlalchemy",
        "flask-migrate",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "requests",
        "raven==6.9.0",
        "blinker",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
