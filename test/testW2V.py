import gensim
import gensim.downloader as api
import pandas as pd
import numpy as np
import gensim.downloader as api

model = api.load("glove-wiki-gigaword-100")

start=["king","woman","man"]
arr = start

tmp = model.most_similar(positive=["kingdom"],topn=10)

lexique = []

for w in tmp:
  lexique.append(w[0])
print(lexique)

simWord = model.most_similar_to_given("man",lexique)



