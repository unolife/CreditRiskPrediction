import requests
import json

server_alive_test = requests.get('http://localhost:8000/')
print(server_alive_test.text)

with open('./sample.json', "r") as json_file:
    predict_response = requests.post('http://localhost:8000/predict', json=json.load(json_file))
    print(predict_response.text)