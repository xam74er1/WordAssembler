from flask import Flask,render_template,make_response
import numpy

from io import BytesIO
import random
from flask import request
import gensim.downloader as api
from flask import jsonify
from flask import json
import json as js

import W2VUtility as w2v
from model.composition_generator import CompositionGenerator

from os import listdir
from os.path import isfile, join

app = Flask(__name__)

app.config.update(
    TESTING=True,
    TEMPLATES_AUTO_RELOAD = True
)

tmp = [f for f in listdir("ressource") if isfile(join("ressource", f))]

allFile =[]
for f in tmp:
    allFile.append(f.replace(".csv",""))

model = api.load("glove-wiki-gigaword-100")

mapCompo = {};
for w in allFile:
    compo = CompositionGenerator([w+".csv"])
    compo.generate()
    mapCompo[w] =compo;

fword = compo.firstWorld()

print("First word ",fword)

#Supervise : on a controle les input et reponce
@app.route('/getCumstomeCloseWord')
def getCustomCloseWord(n=1):
    positve = js.loads(request.args.get('positive'))
    negative = js.loads(request.args.get('negative'))
    print("Positive",positve,"negative",negative)
    fname = request.args.get('fileName')
    print("fname :",fname)
    if(fname==None):
        fname="Kingdom"
    ftype = fname
    print("file name", ftype)
    if ftype != "free":
        compo = mapCompo[ftype]
        res = compo.getWordFormate(positve,negative)
    else:
        res = w2v.getCloseWordCustom(positve, negative, model)

    print("res ",res)
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response

#Non supervise uniqument avec le modelle de W2V
@app.route('/getcloseWord')
def getCloseWord(n=1):

   print(request.is_json)
   positve = js.loads(request.args.get('positive'))
   print("positive",positve)
   negative = js.loads(request.args.get('negative'))
   print("negative",negative)

   res= w2v.getCloseWord(positve,negative,model)
   print(res)
   response = app.response_class(
       response=json.dumps(res),
       status=200,
       mimetype='application/json'
   )
   return response

@app.route('/getword')
def get3dWord(n=42):
   w = request.args.get('word')
   print("word : ",w)
   res= w2v.getCloseWordIn3D(w,model);
   print(res)
   response = app.response_class(
       response=json.dumps(res),
       status=200,
       mimetype='application/json'
   )
   return response



@app.route("/")
def index():
    print("All file ",allFile)
    return render_template("index.html",color="0xff0000",allFile=allFile)

@app.route("/combi")
def combi():
    ftype = request.args.get("type")
    print(ftype)
    if ftype ==None:
        ftype = "Kingdom"
    if ftype=="free":
        fword=["water","air","fire","dirt"]
    else:
      fword = mapCompo[ftype].firstWorld()
    return render_template("combinator.html",fword=fword,allFile=allFile,acutalWord=ftype)

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    color = "0x%06x" % random.randint(0, 0xFFFFFF)
    response = make_response(color)
    return (response)

if __name__ == "__main__":
    import os,sys
    if not os.path.exists("templates/index.html"):
        print("You need to make a 'templates' folder and move index.html there")
        sys.exit(1)
    app.debug = True
    app.run(debug=True, use_reloader=False)