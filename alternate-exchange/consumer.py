import pika
from pika.exchange_type import ExchangeType


def alt_on_message_received(ch, method, properties, body):
    print(f"Alt received: {body}")

def main_on_message_received(ch, method, properties, body):
    print(f"Main received: {body}")   
   
connection_parameters = pika.ConnectionParameters('13.212.224.57')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()



channel.exchange_declare(exchange="altexchange", exchange_type=ExchangeType.fanout)
channel.exchange_declare(
    exchange="mainexchange", 
    exchange_type=ExchangeType.direct, 
    arguments={'alternate-exchange': 'altexchange'})


channel.queue_declare(queue='altexchangequeue')
channel.queue_bind('altexchangequeue', 'altexchange')
channel.basic_consume(
    queue='altexchangequeue', 
    auto_ack=True,
    on_message_callback=alt_on_message_received)  




channel.queue_declare(queue='mainexchangequeue')
channel.queue_bind('mainexchangequeue', 'mainexchange', routing_key='test')
channel.basic_consume(
    queue='mainexchangequeue', 
    auto_ack=True,
    on_message_callback=main_on_message_received)

  

print('Starting Consuming')

channel.start_consuming()