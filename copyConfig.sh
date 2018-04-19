#/bin/bash

for node in node1 node2 node3 node4 node5; do
    scp /etc/hadoop/* $node:/etc/hadoop/;
done

echo "CONFIGS COPIED"