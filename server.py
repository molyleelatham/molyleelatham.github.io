from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import logging

app = Flask(__name__)
CORS(app) 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

API_KEY = '3WDN7B3P4RR7JVLL'

@app.route('/get_sentiment', methods=['POST'])
def get_sentiment():
    try:
        ticker = request.json.get('ticker')
        if not ticker:
            return jsonify({"error": "Ticker not provided"}), 400
        
        url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        return jsonify(data)
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
