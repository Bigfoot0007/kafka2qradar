from kafka import KafkaConsumer

topic="stresstest"
# To consume latest messages and auto-commit offsets
# consumer = KafkaConsumer(topic,group_id='abc1',bootstrap_servers=['9.111.123.20:9092'],auto_offset_reset='earliest')
consumer = KafkaConsumer(topic,bootstrap_servers=['9.111.123.20:9092'],auto_offset_reset='earliest')
print(" Build a consumer....")
# consumer.seek_to_beginning(0)
# print(" Seek to beginning ....")
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
    print(message)


consumer.close()