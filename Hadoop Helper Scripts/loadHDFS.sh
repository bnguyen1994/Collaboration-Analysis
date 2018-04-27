#!/bin/bash

hdfs dfs -mkdir -p /user/hadoop
hdfs dfs -mkdir dblp-ref
hdfs dfs -put dblp-ref/dblp-ref-*.json dblp-ref
hdfs dfs -ls -R /

echo 'END SCRIPT'
