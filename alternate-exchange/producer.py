import pika
import time
import random
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('13.212.224.57')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.exchange_declare(exchange="altexchange", exchange_type=ExchangeType.fanout)
channel.exchange_declare(
    exchange="mainexchange", 
    exchange_type=ExchangeType.direct, 
    arguments={'alternate-exchange': 'altexchange'})


messageID = 1
while(True):
    message = f"alternate-exchange : {messageID}"
    channel.basic_publish(exchange="mainexchange", 
    # routing_key="test", #testing alternate exchange, changing routing key
    routing_key="simple",
    body=message,)
    print(f"sent message: {message}")
    time.sleep(random.randint(1, 4))
    messageID+=1





