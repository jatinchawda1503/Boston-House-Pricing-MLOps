from flask import Flask, render_template, jsonify, request

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as CFG
from boston.infer import Infer

import pandas as pd
import json
import pickle


app = Flask(__name__)
model = pickle.load(open(os.path.join(CFG.get_model_path(), 'model.pkl'), 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    data = pd.DataFrame(data, index=[0])
    infer = Infer(data)
    predictions = infer.get_predictions()
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
    


