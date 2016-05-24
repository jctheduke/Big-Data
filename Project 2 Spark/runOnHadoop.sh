#!/bin/bash
#Defining program variables

#bin/hdfs dfs -mkdir /user
#bin/hdfs dfs -put /home/c/Documents/CS567/senti/imdbErOld.txt /user
#bin/hdfs dfs -put /home/c/Documents/CS567/senti/labeledBow.feat /user

bin/hdfs dfs -rm -r -skipTrash /user/senti-output

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar  \
-mapper ~/Documents/CS567/senti/senti-mapper.py \
-reducer ~/Documents/CS567/senti/senti-reducer.py \
-cacheFile /user/imdbErNew.txt#ref \
-input /user/labeledBow.feat \
-output /user/senti-output

bin/hdfs dfs -cat /user/senti-output/*
