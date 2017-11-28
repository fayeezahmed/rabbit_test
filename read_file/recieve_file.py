import pika 

def callback(ch, method, properties, body):
		print("  [x] Recieved %r" %body)
		ch.basic_ack(delivery_tag = method.delivery_tag)

def read_lines_from_rabbit():
	con = connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = con.channel()
	channel.queue_declare(queue='ReadLines', durable=True)
	channel.basic_consume(callback,
                      queue='ReadLines')
	channel.start_consuming()
					  
if __name__ == "__main__":
	print("Waiting for input...")
	read_lines_from_rabbit()
	