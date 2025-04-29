import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='resultat')

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Résultat reçu : {message}")

channel.basic_consume(queue='resultat',
                      on_message_callback=callback,
                      auto_ack=True)

print("Client résultat en attente...")
channel.start_consuming()