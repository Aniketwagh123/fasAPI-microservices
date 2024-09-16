import pika
import json
import os

def get_rabbitmq_connection():
    connection_params = pika.ConnectionParameters(os.getenv('RABBITMQ_URL', 'amqp://rabbitmq'))
    connection = pika.BlockingConnection(connection_params)
    return connection

def send_message(queue_name, message):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    connection.close()
