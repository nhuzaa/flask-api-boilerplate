from setuptools import setup, find_packages

setup(
    name='app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psycopg2',
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-marshmallow',
        'flask-restful',
        'marshmallow-sqlalchemy'
    ],
)
