FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
