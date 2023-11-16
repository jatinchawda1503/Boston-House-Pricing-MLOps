FROM python:3.11
COPY . /boston-app
WORKDIR /boston-app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app --chdir app