from flask import Flask
from flask_pymongo import pymongo
import ssl
from bson import json_util
import json

app = Flask(__name__)
CONNECTION_STRING = "mongodb+srv://abdullah:abdullah@coffee.2cjjd.mongodb.net/Coffee?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client.get_database('Coffee')
coffee_machines = pymongo.collection.Collection(db, 'coffee_machines')
coffee_products = pymongo.collection.Collection(db, 'coffee_products')


def dict_to_json(result):
    r = json.dumps(result)
    loaded_r = json.loads(r)
    return loaded_r

@app.route('/coffee_machines', methods=['POST'])
def get_all_coffee():
    cursor = coffee_machines.find({})
    result = dict()
    for document in cursor:
        page_sanitized = json.loads(json_util.dumps(document))
        for i in page_sanitized:
            if i != '_id':
                result[i] = page_sanitized[i]
    return dict_to_json(result)

@app.route('/coffee_pods', methods=['POST'])
def get_all_pods():
    cursor = coffee_products.find({})
    result = dict()
    for document in cursor:
        page_sanitized = json.loads(json_util.dumps(document))
        for i in page_sanitized:
            if i != '_id':
                result[i] = page_sanitized[i]
    return dict_to_json(result)

@app.route('/coffee_machines/<product_type>', methods=['POST'])
def get_coffee(product_type):
    result = get_all_coffee()
    _result = dict()
    for key, value in result.items():
        if value['product_type'] == product_type:
            _result[key] = value
    return dict_to_json(result)

@app.route('/coffee_pods/<product_type>', methods=['POST'])
def get_pods(product_type):
    result = get_all_pods()
    _result = dict()
    for key, value in result.items():
        if value['product_type'] == product_type:
            _result[key] = value
    return dict_to_json(_result)

@app.route('/coffee_pods/<product_type>/<coffee_flavor>', methods=['POST'])
def get_pods_filter(product_type, coffee_flavor):
    result = get_all_pods()
    _result = dict()
    for key, value in result.items():
        if value['product_type'] == product_type and value['coffee_flavor'] == coffee_flavor:
            _result[key] = value
    return dict_to_json(_result)

@app.route('/coffee_pods/<product_type>/<coffee_flavor>/<pack_size>', methods=['POST'])
def get_pods_filter2(product_type, coffee_flavor, pack_size):
    result = get_all_pods()
    _result = dict()
    for key, value in result.items():
        if value['product_type'] == product_type and value['coffee_flavor'] == coffee_flavor and value['pack_size'] == pack_size:
            _result[key] = value
    return dict_to_json(_result)

@app.route('/coffee_machines/<product_type>/<water_line>', methods=['POST'])
def get_coffee_filter(product_type, water_line):
    result = get_all_coffee()
    _result = dict()
    for key, value in result.items():
        if value['product_type'] == product_type and str(value['water_line_compatible']) == water_line:
            _result[key] = value
    return dict_to_json(_result)




if __name__ == '__main__' :
    app.run(debug=True)


