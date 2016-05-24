#!/usr/bin/env python

import sys
import numpy.random as rand
import os
from sklearn.datasets import load_svmlight_file
import numpy as np
# input comes from STDIN (standard input)
#f = open("mapOut","w")
scores=[]
wt=[]
def read_cache():
    for line in open('ref'):
        sc=line.strip()
        scores.append(sc)
    wt=np.asarray(scores).astype(float)    
#lines = [line.rstrip('\n') for line in open('/home/c/Downloads/imdbEr.txt')]
#wt=np.asarray(lines).astype(float)
i=0
read_cache()

def _convert(t):
        """Convert feature and value to appropriate types"""
        return (int(t[0]), float(t[1]))
        
for line in sys.stdin:
    i=i+1
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    #X_train,y_train = load_svmlight_file(line,n_features=89527)
    #x=X_train[0]    
    #ourScore=x.dot(wt).max()
    print '%d,%s,%d' % (i,words[0],rand.randint(0,10))
    #print '%d,%s,%f' % (i,words[0],ourScore)
    # use random number here instead the computed score of a document
    # in hadoop, we don't need to write a real output file.

    # c@chen:~/Documents/CS567$ hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar 
    #-mapper ~/Documents/CS567/commCal.py 
    #-reducer ~/Documents/CS567/07/wordcount-reducer.py 
    #-input /user/chen/labeledBow.feat 
    #-output /user/chen/bow-output    
#    f.write(str(i)+","+words[0]+","+str(rand.randint(0,10))+"\n")
#f.close()
