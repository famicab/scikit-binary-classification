import pickle

from flask import Flask, jsonify, request

from predict_service import predict_single

app = Flask('churn-predict')

with open('models/churn-model.pck', 'rb') as f:
    dv, model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    churn, prediction = predict_single(customer, dv, model)

    result = {
        'Converted': bool(churn),
        'converted_probability': float(prediction),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
