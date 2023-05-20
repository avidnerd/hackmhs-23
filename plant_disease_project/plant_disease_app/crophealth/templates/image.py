from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)
snippet = ""
disease_name = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    plant_image = request.files['plantImage']
    image_path = 'uploads/' + plant_image.filename
    plant_image.save(image_path)

#RUN SOFTWARE HERE
#VOID IF NO DISEASE IS FOUND

def search_plant_disease(disease_name):
    api_key = 'AIzaSyDHJ_-UNx41ZcdnzHos6l6Zb7n1cd0gX5A'  
    search_engine_id = 'https://cse.google.com/cse.js?cx=711a8a876e84d4ea4' 
    query = f'{disease_name} plant disease care tips'
    search_url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'
    response = requests.get(search_url)
    search_results = response.json()
    if 'items' in search_results:
        top_result = search_results['items'][0]  
        snippet = top_result['snippet']

def get_result():
    return snippet

def get_render():
    return render_template('results.html', disease=disease_name, care_tips=search_plant_disease(disease_name).snippet)

if __name__ == '__main__':
    app.run()
