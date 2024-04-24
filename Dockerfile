FROM python:3.9-slim-buster

ENV BROKER="myBroker"
ENV TOPIC="random_value"
ENV RATE="5"

ADD requirements.txt .
ADD tp2_data_publisher_base.py .

RUN pip install -r requirements.txt

CMD ["python", "./tp2_data_publisher_base.py"]