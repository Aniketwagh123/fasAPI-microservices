from pymongo import MongoClient
from utils.rabbitmq import get_rabbitmq_connection
from models.payroll import Payroll
from config.settings import DATABASE_URL
import pika
import json

client = MongoClient(DATABASE_URL)
db = client.payroll_db
payroll_collection = db.payrolls

def delete_payrolls_for_employee(employee_id: str):
    payroll_collection.delete_many({"employee_id": employee_id})

def callback(ch, method, properties, body):
    message = json.loads(body)
    if message['action'] == 'delete':
        delete_payrolls_for_employee(message['employee_id'])
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consuming():
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue='payroll_delete_queue', durable=True)
    channel.basic_consume(queue='payroll_delete_queue', on_message_callback=callback)
    channel.start_consuming()

# Start the consumer when the service starts
if __name__ == "__main__":
    start_consuming()
