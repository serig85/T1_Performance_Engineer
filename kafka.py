from pykafka import Producer

print('start ok')
Producer
producer = Producer({"bootstrap.servers": "5.35.10.200:9092"})
producer.produce('first.messages', value= 'val', key = 'zz' )
producer.flush()
