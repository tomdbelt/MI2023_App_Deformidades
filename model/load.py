import numpy as np
import tensorflow as tf
from keras.models import model_from_json
from keras.optimizers import Adam


def init(fruta):
    loaded_model = None
    graph = None
    
    if fruta == 'manzana':
        json_file = open('./model/MobileNetV2_Manzana.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        # Load weights into new model
        loaded_model.load_weights("./model/MobileNetV2_Manzana.h5")
        print("*"*15)
        print("Modelo manzana cargado exitosamente")
        print("*"*15)

        # Compile and evaluate loaded model
        loaded_model.compile(
            optimizer = Adam(learning_rate=0.001),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
        )
        graph = tf.compat.v1.get_default_graph()
        
    elif fruta == 'mango':
        json_file = open('./model/MobileNetV2_Mango.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        # Load weights into new model
        loaded_model.load_weights("./model/MobileNetV2_Mango.h5")
        print("*"*15)
        print("Modelo mango cargado exitosamente")
        print("*"*15)

        # Compile and evaluate loaded model
        loaded_model.compile(
            optimizer = Adam(learning_rate=0.001),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
        )
        graph = tf.compat.v1.get_default_graph()
    
    else:
        json_file = open('./model/MobileNetV2_Fresa.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        # Load weights into new model
        loaded_model.load_weights("./model/MobileNetV2_Fresa.h5")
        print("*"*15)
        print("Modelo fresa cargado exitosamente")
        print("*"*15)

        # Compile and evaluate loaded model
        loaded_model.compile(
            optimizer = Adam(learning_rate=0.001),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
        )
        graph = tf.compat.v1.get_default_graph()

    return loaded_model, graph