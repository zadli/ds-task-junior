from transformers import pipeline
from flask import Flask, request
import json

app = Flask(__name__)

classifier = pipeline("text-classification",model='bhadresh-savani/bert-base-uncased-emotion', return_all_scores=True)

@app.route('/emotion-detection', methods=['POST'])
def main():
	prediction = classifier(str(request.form["s"]), )
	data = {"s": str(request.form["s"]), "out": prediction[0]}
	return data

if __name__ == "__main__":
    app.run(debug=True)
