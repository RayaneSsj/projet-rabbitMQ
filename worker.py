import pika
import json
import sys
import time
import random

operation = sys.argv[1]

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='calcul')
channel.queue_declare(queue='resultat')

def callback(ch, method, properties, body):
    message = json.loads(body)
    n1 = message['n1']
    n2 = message['n2']
    op = message['op']

    if op != operation and op != 'all':
        return

    print(f"Worker {operation} reçoit : {message}")

    result = None
    if operation == 'add':
        result = n1 + n2
    elif operation == 'sub':
        result = n1 - n2
    elif operation == 'mul':
        result = n1 * n2
    elif operation == 'div':
        result = n1 / n2 if n2 != 0 else 'infini'

    time.sleep(random.randint(5, 15))

    message['operation_effective'] = operation
    message['result'] = result

    channel.basic_publish(exchange='',
                          routing_key='resultat',
                          body=json.dumps(message))
    print(f"Résultat envoyé : {message}")

channel.basic_consume(queue='calcul',
                      on_message_callback=callback,
                      auto_ack=True)

print(f"Worker {operation} en attente...")
channel.start_consuming()