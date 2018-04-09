# -*- coding: utf-8 -*-
######################3
##  压力测试使用，在topic “stresstest”中添加10万条数据

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='9.111.123.20:9092')
for i in range(100000):
    producer.send('stresstest', b'Linux(%d)rexec(pam_unix)[26060]: session opened for user as400rex by (uid=0)' % i)
    print(b'Linux(%d)rexec(pam_unix)[26060]: session opened for user as400rex by (uid=0)' % i)
    if((i % 100) == 0):
        producer.flush()
        print("Flushed")

producer.close()