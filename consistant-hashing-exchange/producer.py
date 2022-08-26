import pika
import time
import random


# rabbitmq-plugins enable rabbitmq_consistent_hash_exchange

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare('simplehashing', 'x-consistent-hash')

routing_key_to_hash = 'hash me'
messageID = 1
while(True):
    message = f"consistant hashing exchange: {messageID}"
    channel.basic_publish(
        exchange='simplehashing', 
        routing_key=routing_key_to_hash, 
        body=message)
    print(f"sent message: {message}")
    time.sleep(random.randint(1, 4))
    messageID+=1





