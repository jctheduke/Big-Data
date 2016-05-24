#!/usr/bin/env python

import sys
import os
import csv
import numpy as np
# input comes from STDIN (standard input)
wlist=[]
weights=[]
def read_cache():
    with open('ref') as fp:
        wlist=fp.readlines()
    for item in wlist:
        weights.append(item.strip('\n'))    
i=0
read_cache()

for line in sys.stdin:
    summ=0
    w=0
    c=0
    
    i=i+1
    temp=''.join(line).split(' ')
    score=temp[0]
    calc=temp[1:len(temp)]
    for pair in calc:
        w,c = [int(x) for x in pair.split(":")]
        summ += c* float(weights[w])
    print '%d,%s,%f' % (i,score,summ)

