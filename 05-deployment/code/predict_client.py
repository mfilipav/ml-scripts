#!/usr/bin/env python
# coding: utf-8

import requests

# run with: python3 predict_client.py
url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 24,
    "monthlycharges": 29.85,
    "totalcharges": (24 * 29.85)
}


response = requests.post(url, json=customer).json()
print("response from server: ", response)

if response['churn'] is True:
    print('ACTION: sending promo email to %s' % customer_id)
else:
    print('ACTION: NOT sending promo email to %s' % customer_id)

