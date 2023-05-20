from flask import Flask, render_template, request
import os
import requests
from googlesearch import search

app = Flask('testapp')
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
'''
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
'''
def search_plant_disease(disease):
    query = f"{disease} plant disease care tips"
    num_results = 5  
    search_results = search(query, num_results=num_results, lang='en')
    results = []
    for result in search_results:
        results.append(result)
    return results

index = open("results.html").read().format(disease=disease_name, 
                                         links=search_plant_disease(disease_name))
'''
html_file = "results.html"
with open(html_file, "a") as file:
    file.write("<h1>Search Results for '{disease_name}'</h1>")
    for data in search_plant_disease(disease_name):
         file.write(f"<p>{data}</p>")

def index():
    return render_template('results.html', disease=disease_name, links=search_plant_disease(disease_name))

if __name__ == '__main__':
    app.run()
'''