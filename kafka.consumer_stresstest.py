from kafka import KafkaConsumer
topic="stresstest"
targetfile="kafka.stresstest.out"
kafkaserver=['9.111.123.20:9092']
# To consume latest messages and auto-commit offsets
# consumer = KafkaConsumer(topic,group_id='abc1',bootstrap_servers=['9.111.123.20:9092'],auto_offset_reset='earliest')
consumer = KafkaConsumer(topic,bootstrap_servers=kafkaserver,auto_offset_reset='earliest')

print(" Build a consumer....")

with open(targetfile,"w") as f:
    counter=0
    for message in consumer:
        f.write("%s:%d:%d: key=%s value=%s\n" % (message.topic, message.partition,message.offset, message.key,message.value))
        # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
        # print message.offset,
        if(message.offset==120000):
            print(message,counter)
            break
