import pika
import time
import random
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('13.214.169.24')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="firstexchange", exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange="secondexchange", exchange_type=ExchangeType.fanout)

channel.exchange_bind("secondexchange", "firstexchange")

messageID = 1
while(True):
    message = f"This message has gone through multiple exchanges: {messageID}"
    channel.basic_publish(exchange="firstexchange", routing_key="", body=message)
    print(f"sent message: {message}")
    time.sleep(random.randint(1, 4))
    messageID+=1





