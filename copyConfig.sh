#/bin/bash

for node in Hadoop-Node1 Hadoop-Node2 Hadoop-Node3 Hadoop-Node4 Hadoop-Node5; do
    scp /home/hadoop/hadoop/etc/hadoop/* $node:/home/hadoop/hadoop/etc/hadoop/;
done

echo "CONFIGS COPIED"
