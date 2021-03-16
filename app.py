from flask import Flask,render_template,make_response
import numpy
from stl import mesh
from io import BytesIO
import random
from flask import request
import gensim.downloader as api
from flask import jsonify
from flask import json

from W2VUtility import getCloseWordIn3D, getCloseWord

app = Flask(__name__)

app.config.update(
    TESTING=True,
    TEMPLATES_AUTO_RELOAD = True
)

model = api.load("glove-wiki-gigaword-100")

@app.route('/getcloseWord')
def get3dWord(n=1):
   content = request.get_json()
   print(content)

   positve = request.args.get('positive')
   negative = request.args.get('negative')
   res= getCloseWord(positve,negative,model)
   print(res)
   response = app.response_class(
       response=json.dumps(res),
       status=200,
       mimetype='application/json'
   )
   return response

@app.route('/getword')
def get3dWord(n=1):
   w = request.args.get('word')
   print("word : ",w)
   res= getCloseWordIn3D(w,model);
   print(res)
   response = app.response_class(
       response=json.dumps(res),
       status=200,
       mimetype='application/json'
   )
   return response


@app.route('/object.stl')
def stl_gen(n=1):
    # tetrahedron mesh
    data = numpy.zeros(4, dtype=mesh.Mesh.dtype)
    b1,b2,b3,t = (1,0,1),(0,0,-0.75),(-1,0,1),(0,1,0)
    data['vectors'][0] = numpy.array([b1,b2,b3])
    data['vectors'][1] = numpy.array([b1,b2,t])
    data['vectors'][2] = numpy.array([b2,b3,t])
    data['vectors'][3] = numpy.array([b3,b1,t])
    object_mesh = mesh.Mesh(data, remove_empty_areas=False)

    # numpy-stl does a poor job of being "API" ready..
    # needs a generic string-ready .write method
    # (great opportunity for an open source contribution!)
    # for now we use a file-like object, BytesIO, to fake it out
    output = BytesIO()
    object_mesh._write_ascii(output,"object.stl")
    response = make_response(output.getvalue())
    return response

@app.route("/")
def index():
    return render_template("index.html",color="0xff0000")

@app.route("/combi")
def combi():
    return render_template("combinator.html")

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
    app.run()