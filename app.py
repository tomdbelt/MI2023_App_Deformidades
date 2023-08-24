from flask import Flask, render_template, request
import numpy as np
import keras.models
import re
import sys 
import os
import base64
import cv2
sys.path.append(os.path.abspath("./model"))
from load import * 

global model_manzana, graph_manzana
global model_mango, graph_mango
global model_fresa, graph_fresa

# INIT MODELS
# model_manzana, graph_manzana = init('manzana')
# model_mango, graph_mango = init('mango')
# model_fresa, graph_fresa = init('fresa')

# INIT APP
app = Flask(__name__)

# CUSTOM FUNCTIONS
def prepareImage(imgData1):
    imgstr = re.search(b'base64,(.*)',imgData1).group(1)
    with open('output.png','wb') as output:
	    output.write(base64.b64decode(imgstr))

# ROUTES
@app.route("/")
def index_view():
    return render_template("index.html")
        
@app.route('/predict/<int:fruta_id>',methods=['GET','POST'])
def predict():
    imgData = request.get_data()
    prepareImage(imgData)
    x = imread('output.png',mode='L')
    x = np.invert(x)
    x = imresize(x,(28,28))
    x = x.reshape(1,28,28,1)

    with graph.as_default():
        out = model.predict(x)
        print(out)
        print(np.argmax(out,axis=1))
        
        response = np.array_str(np.argmax(out,axis=1))
        return response	
 
if __name__ == '__main__': 
   app.run(debug=True)