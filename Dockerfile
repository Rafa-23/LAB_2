FROM python:3.9-slim-buster

ENV BROKER="localhost"
ENV TOPIC="random_value"
ENV RATE="5"

ADD tp2_data_publisher_base.py .

RUN pip install requests paho.mqtt.publish

CMD ["python", "./tp2_data_publisher_base.py"]