import pika
import json
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='calcul')

operations = ['add', 'sub', 'mul', 'div', 'all']

while True:
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    op = random.choice(operations)

    message = {
        'n1': n1,
        'n2': n2,
        'op': op
    }

    channel.basic_publish(exchange='',
                          routing_key='calcul',
                          body=json.dumps(message))
    print(f"Envoyé : {message}")

    time.sleep(5)