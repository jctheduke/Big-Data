# imports
from random import random
import csv
from collections import Counter


# lists
wlist = []
weights = []
reviews = []

# save the reviews
csvrd = open(r'C:\Users\priyaranjan\Downloads\aclImdb\train\labeledBow.feat', 'r')
tempReviews = csv.reader(csvrd)
for row in tempReviews:
    reviews.append(row)

# from the Potts 2011 experiment
with open(r'C:\Users\priyaranjan\Downloads\imdbErNew.txt', 'rb') as fp:
    wlist = fp.readlines()
for item in wlist:
    weights.append(item[:-1])

# delete unused variables
del csvrd, wlist


# Actual function which classifies the reviews
def nav(reviews):
    # positive/negative hit rates
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    # initialize
    summ = 0
    w = 0
    c = 0
    # main loop
    # mapper
    FFP=[]     #For storing word count in False postives    
    FFN=[]     #For storing word count in False negative
    TTP=[]
    TTN=[]

    for review in reviews:
        summ = 0
        w = 0
        c = 0
        temp = ''.join(review).split(' ')
        score = temp[0]
        calc = temp[1:len(temp)]
        for pair in calc:
            w, c = [int(x) for x in pair.split(":")]
            summ += c* float(weights[w])
            # print score,summ
        # mapper sends score, summ
        # reducer
        if (int(score) >= 7) and (summ > 0):
            TP += 1
            TTP.append(review)   # Collection of True positives
        if (int(score) <= 4) and (summ <= 0):
            TN += 1
            TTN.append(review)   # Collection of  False postives
        if (int(score) >= 7) and (summ <= 0):
            FN += 1
            FFN.append(review)   # Collection of True positives
        if (int(score) <= 4) and (summ > 0):
            FP += 1
            FFP.append(review)   # Collection of False positives
    
    # results // accuracy, precision, sensitivity, specificity
    acc = float(TP + TN)/(TP+TN+FP+FN)
    prec = float(TP)/(TP+FP)
    sens = float(TP)/(TP+FN)
    spec = float(TN)/(FP+TN)
    print(acc)
    print(FP,FN)
    return (FFP,FFN,TTP,TTN)       # Returning the arrays


def com(F):       # Collects word and their corresponding total counts or total weights
    d=[]
    p={}
    for item in F:
        temp=(str(item)[4:-2]).split(" ")
        for x in temp:
            if len(x)!=0:
                [a,b]=x.split(":")
                d.append([int(a),float(weights[int(a)])*int(b)])  # For aggregating weights
                #d.append([int(a),int(b)])                        # For aggregating no of counts
    for x,y in d:
        p[x]=p.get(x,0.0)+y
    return Counter(p)


for l in range(40):           # No of iterations
    Fp,Fn,Tp,Tn=nav(reviews)  # False and True predictions
    CFp=com(Fp)               # Collects words and their counts for  False predictions
    CFn=com(Fn)
    CTp=com(Tp)               # Collects words and their counts for  True predictions
    CTn=com(Tn)

    l1=CFp.most_common(10000)  # Collection of most common 10000 words and their weights(counts)from false predictions
    l2=CTp.most_common(10000)  # Collection of most common 10000 words and their weights(counts) from true predictions
    l3=CFn.most_common(10000)
    l4=CTn.most_common(10000)



    l1=[x[0] for x in l1]       #Collection of only most common words
    l2=[x[0] for x in l2]
    l3=[x[0] for x in l3]
    l4=[x[0] for x in l4]
    l5=(l1+l2+l3+l4)
    l6=Counter(l5)
    l6=l6.most_common(1000)     #Most 1000 common words in all catagories
    l7=[x[0] for x in l6]

    g1=(set(l1)-set(l4))      #Filtering out the words from False prediction which are present in True predictions
    g2=(set(l3)-set(l2))


    print(len(g1))            # prints the number of uncommon words
    weights1=weights          #Stores current weights


    for x in l7:
        weights[x]= bytes(str(float(weights[x])*0.95),'ascii')      # This will decrease the weight a little of top 1000  common words
    for x in g1:
        weights[x]= bytes(str(float(weights[x])*0.71),'ascii')      # This will decrease the weight of false positives
    for x in g2:
        weights[x]=bytes(str(float(weights[x])*1.3),'ascii')        # Increaseing the weight of False negatives
nav(reviews)                                                        # Calculating accuracy with new weights