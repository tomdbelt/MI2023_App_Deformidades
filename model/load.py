import numpy as np
import keras.models
from keras.models import model_from_json
import tensorflow as tf


def init(fruta):
    loaded_model = None
    graph = None
    
    if fruta == 'manzana':
        json_file = open('model_manzana.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        # Load weights into new model
        loaded_model.load_weights("model_manzana.h5")
        print("Loaded Model from disk")

        # Compile and evaluate loaded model
        loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        graph = tf.get_default_graph()
        
    elif fruta == 'mango':
        json_file = open('model_mango.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        # Load weights into new model
        loaded_model.load_weights("model_mango.h5")
        print("Loaded Model from disk")

        # Compile and evaluate loaded model
        loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        graph = tf.get_default_graph()
    
    else:
        json_file = open('model_fresa.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        # Load weights into new model
        loaded_model.load_weights("model_fresa.h5")
        print("Loaded Model from disk")

        # Compile and evaluate loaded model
        loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        graph = tf.get_default_graph()
    

	# json_file = open('model.json','r')
	# loaded_model_json = json_file.read()
	# json_file.close()
	# loaded_model = model_from_json(loaded_model_json)
	# #load weights into new model
	# loaded_model.load_weights("model.h5")
	# print("Loaded Model from disk")

	# #compile and evaluate loaded model
	# loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	# #loss,accuracy = model.evaluate(X_test,y_test)
	# #print('loss:', loss)
	# #print('accuracy:', accuracy)
	# graph = tf.get_default_graph()
    return loaded_model, graph