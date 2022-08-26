import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f"received: {body}")
   
connection_parameters = pika.ConnectionParameters('13.214.169.24')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="headerexchange", exchange_type=ExchangeType.headers)
channel.queue_declare("letterbox")

# Binding Arguments	   Receives Message?
# type: report
# format: pdf
# x-match: all	            Yes
# type: report
# format: docx
# x-match: all	            No
# type: report
# format: pdf
# x-match: any	            Yes

bind_args = {
    'x-match': 'any',
    'name' : 'nahid',
    'age' : '23',
    'location' : 'Malaysia'
}

channel.queue_bind('letterbox', 'headerexchange', arguments=bind_args)


channel.basic_consume(
    queue='letterbox', 
    auto_ack=True,
    on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()