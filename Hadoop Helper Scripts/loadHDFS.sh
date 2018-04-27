#!/bin/bash

echo 'Creating hadoop user directory. . .'
hdfs dfs -mkdir -p /user/hadoop
echo 'Creating dblp-ref directory. . .'
hdfs dfs -mkdir dblp-ref
echo 'Loading dblp-ref-*.json files. . .'
hdfs dfs -put dblp-ref/dblp-ref-*.json dblp-ref
echo 'Listing hdfs directory. . .'
hdfs dfs -ls -R /

echo 'END SCRIPT'
