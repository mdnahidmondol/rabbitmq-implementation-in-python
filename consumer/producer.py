import pika
import time
import random

connection_parameters = pika.ConnectionParameters('13.214.190.7')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue="letterbox")

messageID = 1
while(True):
    message = f"Sending messageID: {messageID}"
    channel.basic_publish(exchange="", routing_key="letterbox", body=message)
    print(f"sent message: {message}")
    time.sleep(random.randint(1, 4))
    messageID+=1





