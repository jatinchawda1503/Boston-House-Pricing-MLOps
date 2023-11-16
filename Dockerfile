FROM python:3.11
COPY . /boston-app 
WORKDIR /boston-app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD web: gunicorn boston-app:app --chdir app