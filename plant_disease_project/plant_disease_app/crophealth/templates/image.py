from flask import Flask, render_template, request
import os
import requests
from googlesearch import search

app = Flask(__name__)
snippet = ""
disease_name = ""

@app.route('/process', methods=['POST'])
def process():
    plant_image = request.files['plantImage']
    image_path = 'uploads/' + plant_image.filename
    plant_image.save(image_path)

#RUN SOFTWARE HERE
#VOID IF NO DISEASE IS FOUND
disease_name="apple black rot"

def search_plant_disease(disease):
    query = f"{disease} plant disease care tips"
    num_results = 5  
    search_results = search(query, num_results=num_results, lang='en')
    results = []
    for result in search_results:
        results.append(result)
    return results

@app.route('/process', methods=['POST'])
def process():
    disease_name = request.form['disease_name']
    links = search_plant_disease(disease_name)
    return render_template('results.html', disease=disease_name, links=links)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()