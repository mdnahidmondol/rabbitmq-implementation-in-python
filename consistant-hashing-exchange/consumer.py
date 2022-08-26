import pika



def on_message1_received(ch, method, properties, body):
    print(f"queue 1 received: {body}")

def on_message2_received(ch, method, properties, body):
    print(f"queue 2 received: {body}")


connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare('simplehashing', 'x-consistent-hash')


channel.queue_declare(queue="letterbox1")
channel.queue_declare(queue="letterbox2")


channel.queue_bind('letterbox1', 'simplehashing', routing_key='1')
channel.basic_consume(
    queue='letterbox1', 
    auto_ack=True,
    on_message_callback=on_message1_received)


channel.queue_bind('letterbox2', 'simplehashing', routing_key='4')
channel.basic_consume(
    queue='letterbox2', 
    auto_ack=True,
    on_message_callback=on_message2_received)

print('Starting Consuming')

channel.start_consuming()