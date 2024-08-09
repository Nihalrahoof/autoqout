from flask import Flask, request, jsonify, send_from_directory

import customers_dao
import quotation_dao
from sql_connection import get_sql_connection
import mysql.connector
import json
import os  # Import the os module

import products_dao
import uom_dao

app = Flask(__name__, static_folder='ui', static_url_path='')

connection = get_sql_connection()



@app.route('/')
def index():
    return send_from_directory('ui', 'index.html')

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('ui/css', filename)



@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getCustomers', methods=['GET'])
def get_customers():
    response = customers_dao.get_customers(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getlists', methods=['GET'])
def get_lists():
    response = {}
    try:
        response['products'] = products_dao.get_all_products(connection)

        response['quotations'] = quotation_dao.get_all_quotation(connection)

    except Exception as e:
        response['error'] = str(e)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/insertQuotations', methods=['POST'])
def insert_quotation():
    request_payload = json.loads(request.form['data'])
    quotation_id = quotation_dao.insert_new_quotation(connection, request_payload)
    response = jsonify({
        'quotation_id': quotation_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/insertCustomers', methods=['POST'])
def insert_customer():
    request_payload = json.loads(request.form['data'])
    customer_id = customers_dao.insert_new_customers(connection, request_payload)
    response = jsonify({
        'customer_id': customer_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/deleteQuotation', methods=['POST'])
def delete_quotation():
    return_id = quotation_dao.delete_quotation_from_db(connection, request.form['quotation_id'])
    response = jsonify({
        'quotation_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    print(f"Starting Python Flask Server For Grocery Store Management System on port {port}")
    app.run(host='0.0.0.0', port=port)


