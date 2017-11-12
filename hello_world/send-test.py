import pika

con = connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = con.channel()

channel.queue_declare(queue='Greetings')

channel.basic_publish(exchange='', routing_key='hello', body='hello world!')

print(" Sent 'hello world!'")

con.close()
