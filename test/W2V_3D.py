import gensim
import gensim.downloader as api
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

model = api.load("glove-wiki-gigaword-100")

close_words = model.most_similar(positive=["kingdom"],topn=10)
res = [];
for (k,v ) in close_words:
    res.append(k)
X = model[res]
pca = PCA(n_components=3)
result = pca.fit_transform(X)
print(result)