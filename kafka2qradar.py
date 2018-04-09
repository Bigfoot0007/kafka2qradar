#!/usr/bin/env python
# encode = utf8
from kafka import KafkaConsumer
import socket
topic="stresstest"
targetfile="kafka.stresstest.out"
kafkaserver=['9.111.123.20:9092']
qradarserver="9.111.123.29"
# qradarserver="127.0.0.1"

if __name__ == '__main__':
    # consumer = KafkaConsumer(topic,group_id='qradar',bootstrap_servers=kafkaserver)
    consumer = KafkaConsumer(topic,bootstrap_servers=kafkaserver,auto_offset_reset='earliest')
    print(" Built a consumer successful....",kafkaserver)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(" Built a QRadar UDP Connection successful....",qradarserver)
    
    for message in consumer:
        s.sendto(message.value, (qradarserver, 514))
        # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
        # print message.offset,
        if(message.offset==100000):
            print(message)
            break
