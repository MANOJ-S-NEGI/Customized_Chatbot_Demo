from flask import Flask, render_template, request, jsonify
from components.prediction_pipeline import *
import random

app = Flask(__name__)

print('initiating')


@app.route('/', methods=['GET'])
def Home():
    return render_template("index22.html")


@app.route('/predict', methods=['POST'])
def predict():

    input_data = request.form['textarea']
    print(input_data)
    pred_class, json_file = pipeline(input_data)

    for intent in json_file['intents']:
        if intent['tag'] == pred_class:
            bot_response = random.choice(intent['responses'])
            return jsonify(bot_response)
            # return render_template('index.html',input_data=input_data, prediction_texts=response_text)
            # return response_text


if __name__ == '__main__':
    app.run(debug=True)





