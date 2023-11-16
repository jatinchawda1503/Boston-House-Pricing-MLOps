FROM python:3.11
COPY . .
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD web: gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app --chdir app