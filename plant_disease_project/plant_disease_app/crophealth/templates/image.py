from flask import Flask, render_template, request
import os
import requests
from googlesearch import search
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.applications.vgg16 import VGG16
from keras.layers import Dense
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

disease_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Background_without_leaves', 'Blueberry___healthy', 'Cherry___Powdery_mildew',  ]
app = Flask(__name__)
snippet = ""
disease_name = ""

@app.route('/process', methods=['GET', 'POST'])
def process():
	plant_image = request.files['plantImage']
	image_path = 'uploads/' + plant_image.filename
	plant_image.save(image_path)
	image = plant_image.img_to_array(plant_image)
	image = np.expand_dims(image, axis=0)
	
model = VGG16(weights=None, include_top=False, input_shape=(224, 224, 3))
fin_model = Sequential()
fin_model.add(model)
fin_model.add(Dense(39, activation='softmax'))
fin_model.load_weights('/plant_disease_project/plant_disease_app/crophealth/cnn_model/plant_doctor_model_weights.h5')
img = image.load_img()
img_arr = image.img_to_array(img)
processed_img = preprocess_input(img_arr)
input_data = np.expand_dims(processed_img axis=0)
predictions = fin_model.predict(input_data)
predicted_index = np.argmax(predictions)
predicted_label = class_labels[predicted_index]

def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)

def search_plant_disease(disease):
	query = f"{disease} plant disease care tips"
	num_results = 5  
	search_results = search(query, num_results=num_results, lang='en')
	results = []
	for result in search_results:
		results.append(result)
	return results

@app.route('/processer', methods=['POST'])
def processer():
	disease_name = request.form['disease_name']
	links = search_plant_disease(disease_name)
	return render_template('results.html', disease=disease_name, links=links)

@app.route('/')
def index():
	return render_template('home.html')

if __name__ == '__main__':
	app.run()