FROM python AS builder

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV HOSTNAME "0.0.0.0"

CMD ["python", "/app/app.py", "--port", "80"]