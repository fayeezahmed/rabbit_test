import pika

def read_file(text_file):
	with open(text_file, 'r') as f:
		lines = f.readlines()[0].split(".")
		
	return lines
	
def send_lines_to_rabbit(lines):
	con = connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = con.channel()

	channel.queue_declare(queue='ReadLines', durable=True)
	
	for l in lines:
		channel.basic_publish(exchange='', routing_key='ReadLines', body=l)

	print("All sent!")

	con.close()
	

if __name__ == "__main__":
	lines = read_file("loreum.txt")
	send_lines_to_rabbit(lines)
