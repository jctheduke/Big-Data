# imports
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
#with open(r'‪C:\Users\priyaranjan\Downloads\imdbEr.txt', 'rb') as fp:
    wlist = fp.readlines()
for item in wlist:
    weights.append(item[:-1])
# delete unused variables
del csvrd, wlist
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
    FFP=[]
    FFN=[]
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
    return (FFP+FFN,TTP+TTN) # Returning the arrays


F,T=nav(reviews)  # False and True predictions
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
CF=com(F)               # Collects words and their counts for  False predictions
CT=com(T)               # Collects words and their counts for  True predictions 
l1=CF.most_common(10000)  # Collection of most common 10000 words from false predictions
l2=CT.most_common(10000)  # Collection of most common 10000 words from true predictions

l1=[x[0] for x in l1]
l2=[x[0] for x in l2]

l3=(set(l1)-set(l2))      # Filtering out the words from False prediction which are present in True predictions
print(len(l3))            # prints the number of uncommon words 
for x in l3:
    weights[x]=0          # Nuetralizing the words which accounts for False predictions

nav(reviews)              # Calculating accuracy with new weights 