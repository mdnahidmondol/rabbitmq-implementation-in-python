import pika
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('13.212.224.57')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.exchange_declare(
    exchange="acceptrejectexchange", 
    exchange_type=ExchangeType.fanout)



messageID = 1
while(True):
    message = f"Accept Reject exchange testing .... : {messageID}"
    channel.basic_publish(exchange="acceptrejectexchange", 
    routing_key="artest",
    body=message,)
    print(f"sent message: {message}")
    messageID+=1
    input('Press any key to continue ...')





