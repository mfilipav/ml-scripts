import pickle
from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('churn')
"""
For production, use WSGI server, like gunicorn:
$ gunicorn --bind 0.0.0.0:9696 predict_server:app
"""


@app.route('/predict', methods=['POST'])
def predict():
    # extract json from customer request body
    customer = request.get_json()
    print("predict server received customer: ", customer)

    # do the prediction
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    print("predict done, result=", result)
    return jsonify(result)


if __name__ == "__main__":
    # gunicorn doesn't care
    app.run(debug=True, host='0.0.0.0', port=9696)
