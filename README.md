# kafka2qradar


```
Step 1: Download the code
Download the 1.1.0 release and un-tar it.
    > tar -xzf kafka_2.11-1.1.0.tgz
    > cd kafka_2.11-1.1.0
    
    
Step 2: 启动服务器


    bin/zookeeper-server-start.sh config/zookeeper.properties
    bin/kafka-server-start.sh config/server.properties

Step 3: 创建一个Topic

    bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
    bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stresstest
    bin/kafka-topics.sh --list --zookeeper localhost:2181
    bin/kafka-topics.sh --list --zookeeper localhost:2181


```
