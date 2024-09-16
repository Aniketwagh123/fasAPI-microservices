import pika
import json
from utils.rabbitmq import get_rabbitmq_connection

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Processing message: {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consuming():
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue='payroll_queue', durable=True)
    channel.basic_consume(queue='payroll_queue', on_message_callback=callback)
    channel.start_consuming()


    # RPC 
