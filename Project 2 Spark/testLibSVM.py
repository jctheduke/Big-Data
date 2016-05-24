from sklearn.datasets import load_svmlight_file
import numpy as np

X_train,y_train = load_svmlight_file("/home/c/Documents/CS567/labeledBow.feat")
lines = [line.rstrip('\n') for line in open('/home/c/Downloads/imdbEr.txt')]
wt=np.asarray(lines).astype(float)
x=X_train[0]

x.dot(wt)


