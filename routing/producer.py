
import pika
import time
import random
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('13.214.190.7')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)

messageID = 1
while(True):
    message = f"hello, This message needs to be routed: {messageID}"
    messageGenerate = random.randint(1, 4)
    print(messageGenerate)
    if  messageGenerate == 1:
        channel.basic_publish(exchange="routing", routing_key="paymentsonly", body=message)
    elif messageGenerate == 2:
        channel.basic_publish(exchange="routing", routing_key="shop", body=message)
    else:
        channel.basic_publish(exchange="routing", routing_key="analytics", body=message)
    print(f"sent message: {message}")
    time.sleep(random.randint(1, 4))
    messageID+=1

