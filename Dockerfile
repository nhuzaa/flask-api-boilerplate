FROM python:3
COPY ./ ./
RUN pip install gunicorn
RUN python setup.py install
CMD ["gunicorn", "--config", "gunicorn_config.py", "app.wsgi:application"]
EXPOSE 5000
