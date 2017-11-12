import pika

con = connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = con.channel()

channel.queue_declare(queue='Greetings')

def callback(ch, method, properties, body):
    print("  [x] Recieved %r" %body)


channel.basic_consume(callback,
                      queue='hello',
					  no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
