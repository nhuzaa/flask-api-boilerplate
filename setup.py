from setuptools import setup, find_packages

setup(
    name="app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "psycopg2-binary",
        "flask",
        "flask-sqlalchemy",
        "flask-migrate",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "requests",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
