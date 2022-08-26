from ast import arg
import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f"Dead_latter received: {body}")

   
connection_parameters = pika.ConnectionParameters('13.212.224.57')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()



channel.exchange_declare(exchange="mainexchange", exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange="deadlatterexchange", exchange_type=ExchangeType.fanout)




channel.queue_declare(queue='mainexchangequeue',
    arguments={'x-dead-letter-exchange': 'deadlatterexchange', 'x-message-ttl': 5000})
channel.queue_bind('mainexchangequeue', 'mainexchange', routing_key='test')




channel.queue_declare(queue='deadletterqueue')
channel.queue_bind('deadletterqueue', 'deadlatterexchange')
channel.basic_consume(
    queue='deadletterqueue', 
    auto_ack=True,
    on_message_callback=on_message_received)

  

print('Starting Consuming')

channel.start_consuming()