#!/usr/bin/env python

from operator import itemgetter
import sys
from enum import Enum
import numpy as np
class RevClass(Enum):
    positive=1
    negative=-1
    neutral=0
    
confusionArray=[0,0,0,0]    
total=0
falseNeg=[]
falsePos=[]
def classifyGT(score):
    if score >= 7:
        scoreClass = RevClass.positive
    elif score <= 4:
        scoreClass = RevClass.negative
    else:
        scoreClass = RevClass.neutral
    return scoreClass
    
def classifyCS(score):
    if score > 0:
        scoreClass = RevClass.positive
    elif score < 0:
        scoreClass = RevClass.negative
    else:
        scoreClass = RevClass.neutral
    return scoreClass
    
def updateConfusion(GT, CS):
    error = False
    if GT == RevClass.positive:
        if CS == RevClass.positive:
            confusionArray[0] += 1
        else:
            confusionArray[1] += 1
            error = True
    elif GT == RevClass.negative:
        if CS == RevClass.negative:
            confusionArray[3] += 1
        else:
            confusionArray[2] += 1
            error = True
    else:
        error = True
    return error    

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    total+=1
    # parse the input we got from mapper.py
    docid,gt,cs = line.split(",")

    # convert count (currently a string) to int
    try:
        docid = int(docid)
        gt = int(gt)
        cs = float(cs)    
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
        
    GTclass = classifyGT(gt)
    CSclass = classifyCS(cs)
    error = updateConfusion(GTclass, CSclass)    
    if error==True:
        if GTclass == RevClass.positive:
            falseNeg.append(docid)
        if GTclass == RevClass.negative:
            falsePos.append(docid)
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    #print '%d\t%d\t%d' % (docid,gt,cs)
    
confusionPer=np.divide(np.array(confusionArray).astype(float), total)
cM=np.reshape(confusionPer,(-1,2))
#print falseNeg
#print falsePos
print '%d comments\n' % (total) 
print(np.reshape(confusionArray,(-1,2)))    
print(cM)

