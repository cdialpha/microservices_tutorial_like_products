import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters("amqps://fhjyropt:stFwQChX1zdHmxnskO4Yq80YM58zePnA@moose.rmq.cloudamqp.com/fhjyropt")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body): 
    id =json.loads(body)
    product = Product.objects.get(id=id)
    product.likes =  product.likes + 1
    product.save()
    print(f'Received in Admin. Product {id} likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()