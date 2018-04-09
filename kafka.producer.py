from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='9.111.123.20:9092')
for _ in range(100):
    producer.send('test', b'some_message_bytes')

# Block until a single message is sent (or timeout)
future = producer.send('test', b'another_message')
result = future.get(timeout=60)

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()

# Use a key for hashed-partitioning
producer.send('test', key=b'foo', value=b'bar')

# Serialize json messages
import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('fizzbuzz', {'foo': 'bar'})

# Serialize string keys
producer = KafkaProducer(key_serializer=str.encode)
producer.send('flipflap', key='ping', value=b'1234')

>>> # Compress messages
>>> producer = KafkaProducer(compression_type='gzip')
>>> for i in range(1000):
...     producer.send('test', b'msg %d' % i)

>>> # Get producer performance metrics
>>> metrics = producer.metrics()
