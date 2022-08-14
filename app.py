import requests
import json
from flask import Flask
from flask import render_template
import os

NYTAPIKEY = os.getenv('NYTAPI')
API_URL = f"https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={NYTAPIKEY}"
#get_api = f"https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=Aurpqp9qVGhvc0jNuua3poGPvPEGU938"

app = Flask(__name__)

@app.route('/')
def get_articles():
  response = requests.get(API_URL)
  data = response.text
  print(type(data))
  parse_json = json.loads(data)
  print(type(parse_json))

  retrieved_articles = parse_json["results"]
  is_ok = response.ok

  return render_template('index.html', values=retrieved_articles)
  #return "Hellow word"

if __name__ == '__main__':
    app.run(debug=True)