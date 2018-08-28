from setuptools import setup, find_packages

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'psycopg2-binary',
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'requests'
    ],
)
