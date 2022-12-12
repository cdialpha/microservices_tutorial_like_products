import pika, json

params = pika.URLParameters("amqps://fhjyropt:stFwQChX1zdHmxnskO4Yq80YM58zePnA@moose.rmq.cloudamqp.com/fhjyropt")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body): 
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
