import pika
import time
import random
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('13.214.169.24')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.exchange_declare(exchange="headerexchange", exchange_type=ExchangeType.headers)


data = {
    "name" : "nahid",
    "age" : "23",
    "location" : "Malaysia",
    "zipcode" : "40223"
}

messageID = 1
while(True):
    key, value = random.choice(list(data.items()))
    message = f"This message will be sent with this {key}, {value} headers: {messageID}"
    
    channel.basic_publish(exchange="headerexchange", 
    routing_key="",
    body=message,
    properties=pika.BasicProperties(headers={f"{key}": f"{value}"}))
    print(f"sent message: {key}, {value}: {message}")
    time.sleep(random.randint(1, 4))
    messageID+=1





