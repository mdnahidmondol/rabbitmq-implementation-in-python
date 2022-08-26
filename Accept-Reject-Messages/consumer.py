from multiprocessing.connection import deliver_challenge
import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    #manaully ack 
    # ch.basic_ack(delivery_tag=method.delivery_tag, multiple=False)
    if(method.delivery_tag % 5 == 0):
        ch.basic_ack(delivery_tag=method.delivery_tag, multiple=False)
    print(f"received: {body}")

   
connection_parameters = pika.ConnectionParameters('13.212.224.57')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.exchange_declare(exchange="acceptrejectexchange", exchange_type=ExchangeType.fanout)


channel.queue_declare(queue='acceptrejectqueue')
channel.queue_bind('acceptrejectqueue', 'acceptrejectexchange', routing_key='artest')
channel.basic_consume(
    queue='acceptrejectqueue', 
    on_message_callback=on_message_received)



print('Starting Consuming')

channel.start_consuming()