#Please change file locations correspondingly
f1=open('/home/c/Documents/CS567/senti/imdb.vocab','r')
w1=f1.readlines()  # Set of the given vocabulary
f2=open('/home/c/Documents/CS567/senti/imdbEROld.txt','r')
w2=f2.readlines()  # values corresponding to given text
fs=open('/home/c/Documents/CS567/senti/stops.txt','r')
for i in stops:
    try:
        w2[w1.index(i)]='0\n'
    except:
        pass
f3=open('/home/c/Documents/CS567/senti/imdbErNew.txt','w')
for x in w2:
    f3.write(x)
f1.close()
f2.close()
f3.close()
fs.close()
