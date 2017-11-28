import pika

print("Going to send a message..")
con = connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = con.channel()

channel.queue_declare(queue='Greetings', durable=True)

channel.basic_publish(exchange='', routing_key='Greetings', body='hello world!', properties=pika.BasicProperties(delivery_mode = 2))

print(" Sent 'hello world!'")

con.close()
