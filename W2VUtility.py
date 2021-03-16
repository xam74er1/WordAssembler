import gensim
import gensim.downloader as api
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def getCloseWordIn3D(word,model,nb=10):
    #Traiment des mot les plus proche
    close_words = model.most_similar(positive=[word], topn=nb)
    print(close_words)
    res = [];
    for (k, v) in close_words:
        res.append(k)
    res.append(word)
    X = model[res]
    pca = PCA(n_components=3)
    res = pca.fit_transform(X)
    toReturn = {}
    i = 0;
    listWordVect = {}

    for (k, v) in close_words:
        tmp = res[i]
        listWordVect[k] = [float(tmp[0]),float(tmp[1]),float(tmp[2])]
        i+=1
    tmp = res[i]
    listWordVect[word] = [float(tmp[0]),float(tmp[1]),float(tmp[2])]



    toReturn["word"] = word
    toReturn["listWordVect"] =listWordVect;



    return toReturn

def getCloseWord(postive,negative,model):
    return model.most_similar(positive=postive,negative=negative, topn=1)

