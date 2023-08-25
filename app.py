from flask import Flask, render_template, request, redirect, url_for
import numpy as np
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
model_manzana, graph_manzana = init('manzana')
model_mango, graph_mango = init('mango')
model_fresa, graph_fresa = init('fresa')

# INIT APP
app = Flask(__name__)

# CUSTOM FUNCTIONS
def prepareImage(imgData1):
    imgstr = re.search(b'base64,(.*)',imgData1).group(1)
    with open('output.png','wb') as output:
	    output.write(base64.b64decode(imgstr))

# ROUTES
@app.route("/", methods=['GET','POST'])
def index_view():
    if request.method == 'POST':
        selectedFruit = request.form['r_fruit']
        f = open("selectedFruit.txt", "w")
        f.write(selectedFruit)
        f.close()
        clase, prob = predict(selectedFruit)
        img = request.files["fruit_image"]
        
        return render_template('index.html', class_prediction=clase, prob_prediction=prob)
    return render_template("index.html")
        
def predict(selectedFruit):
    if selectedFruit == "manzana":
        print("manzana")
    elif selectedFruit == "mango":
        print("mango")
    else:
        print("fresa")
    
    return 0,0

 
if __name__ == '__main__': 
   app.run(debug=True)