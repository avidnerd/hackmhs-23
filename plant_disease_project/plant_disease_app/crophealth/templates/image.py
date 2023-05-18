from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    plant_image = request.files['plantImage']
    image_path = 'uploads/' + plant_image.filename
    plant_image.save(image_path)
    #IMAGE RECOGNITION SOFTWARE HERE
    return render_template('results.html', disease=disease_name, care_tips=care_tips)
if __name__ == '__main__':
    app.run()
