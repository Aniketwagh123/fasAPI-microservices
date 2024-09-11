import pika
import os

def get_rabbitmq_connection():
    connection_params = pika.ConnectionParameters(os.getenv('RABBITMQ_URL', 'amqp://rabbitmq'))
    connection = pika.BlockingConnection(connection_params)
    return connection
