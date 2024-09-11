import os

DATABASE_URL = os.getenv('DATABASE_URL', 'mongodb://mongo:27017/employee_db')
RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://rabbitmq')
