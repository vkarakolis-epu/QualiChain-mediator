import os

# DOBIE Settings
DOBIE_HOST = os.environ.get('DOBIE_HOST', 'localhost')
DOBIE_PORT = os.environ.get('DOBIE_PORT', 9006)


# RABBITMQ Settings
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT', 5672)
RABBITMQ_VHOST = os.environ.get('RABBITMQ_VHOST', '/')
RABBITMQ_USER = os.environ.get('RABBITMQ_USER', 'rabbitmq')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD', 'rabbitmq')

# APPLICATIO Settings
APP_QUEUE = os.environ.get("mediator_queue")