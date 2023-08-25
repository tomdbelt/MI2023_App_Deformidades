from flask import Flask, render_template, request, redirect, url_for
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import sys 
import os
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
target_img = os.path.join(os.getcwd() , 'static/to_predict')

# INIT APP
app = Flask(__name__)

# CUSTOM FUNCTIONS
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

def square_imgs(img): 
    height, width, channels = img.shape
    value_pixel_init = img[0,0]
    value_pixel_end = img[-1,-1]
    
    is_portrait = True
    square_size = max(height, width)
    if width > height:
        is_portrait = False
        
    # Construir imagen cuadrada
    r = np.zeros((int(square_size),int(square_size)), dtype='uint8')
    g = np.zeros((int(square_size),int(square_size)), dtype='uint8')
    b = np.zeros((int(square_size),int(square_size)), dtype='uint8')

    new_img = cv2.merge((b,g,r))
    space = 0
    fill = 0
    
    if is_portrait:
        space = square_size - width
        fill = int(space/2)
        new_img[: , :fill+1] = value_pixel_init
        new_img[: , fill:fill+width] = img
        new_img[: , fill+width:] = value_pixel_end
    else:
        space = square_size - height
        fill = int(space/2)
        new_img[:fill+1 , :] = value_pixel_init
        new_img[fill:fill+height , :] = img
        new_img[fill+height: , :] = value_pixel_end
        
    return new_img

# Function to load and prepare the image in right shape
def read_image(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

# ROUTES
@app.route("/", methods=['GET','POST'])
def index_view():
    if request.method == 'POST':
        selectedFruit = request.form['r_fruit']
        file = request.files['fruit_image']
        clase, prob, user_img = predict(selectedFruit, file)
        
        return render_template('index.html', class_prediction=clase, prob_prediction=prob, image=user_img)
    return render_template('index.html', class_prediction="", prob_prediction=0, image=None)
        
def predict(selectedFruit, file):
    class_prediction = ""
    prob_prediction = 0
    filename = ""

    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(target_img, filename)
        file.save(file_path)

        img = cv2.imread(file_path)
        img = square_imgs(img)
        img = cv2.resize(img, (224, 224))
        cv2.imwrite(file_path, img)      
        img = read_image(img)

        if selectedFruit == "manzana":
            result=model_manzana.predict(img) 
            classes_x=np.argmax(result,axis=1)
            prob_prediction = result[0][classes_x] * 100
            if classes_x == 0:
              class_prediction = "EXTRA"
            elif classes_x == 1:
              class_prediction = "CLASE 1"
            elif classes_x == 2:
              class_prediction = "CLASE 2"
            else:
              class_prediction = "SIN CLASE"

        elif selectedFruit == "mango":
            result=model_mango.predict(img) 
            classes_x=np.argmax(result,axis=1)
            prob_prediction = result[0][classes_x] * 100
            if classes_x == 0:
              class_prediction = "EXTRA"
            elif classes_x == 1:
              class_prediction = "CLASE 1"
            elif classes_x == 2:
              class_prediction = "CLASE 2"
            else:
              class_prediction = "SIN CLASE"

        else:
            result=model_fresa.predict(img) 
            classes_x=np.argmax(result,axis=1)
            prob_prediction = result[0][classes_x] * 100
            if classes_x == 0:
              class_prediction = "CLASE 1"
            elif classes_x == 1:
              class_prediction = "CLASE 2"
            elif classes_x == 2:
              class_prediction = "EXTRA"
            else:
              class_prediction = "SIN CLASE"
    
    return class_prediction, prob_prediction, filename

 
if __name__ == '__main__': 
   app.run(debug=True)