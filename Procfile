web: python -m spacy download en;gunicorn -b 0.0.0.0:$PORT app.main:application --worker-class=gthread -w 1 --reload
