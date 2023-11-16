FROM python:3.9
COPY . /boston_app
WORKDIR /boston_app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app --chdir /boston_app/app