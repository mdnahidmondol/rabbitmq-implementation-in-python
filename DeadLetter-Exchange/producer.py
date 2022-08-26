import pika
import time
import random
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('13.212.224.57')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.exchange_declare(exchange="mainexchange", exchange_type=ExchangeType.direct)



messageID = 1
while(True):
    message = f"This ,message will expire .... : {messageID}"
    channel.basic_publish(exchange="mainexchange", 
    routing_key="test",
    body=message,)
    print(f"sent message: {message}")
    time.sleep(5)
    messageID+=1





