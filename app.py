import os 
import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.db.conn import getData
from src.services.prediction_pipeline import predictionPerform

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the 'id' parameter from the request body
        data = request.get_json()
        id = data.get('id', None)

        if id is None:
            return jsonify({"error": "Missing 'id' parameter"})

        result = predictionPerform(id)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)