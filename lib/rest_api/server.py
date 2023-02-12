"""Module contains REST api server implementation"""
from flask import Flask, jsonify, request
from flask_cors import cross_origin

from lib.rest_api.server_backup import ServerBackup
from lib.rest_api.server_data import ServerData

app = Flask(__name__)

server_data = ServerData()


@app.route('/')
def index():
    """home page"""
    return "INDEX"


@app.route('/shopping_list')
@cross_origin()
def get_items():
    """Get all items from shopping list in json format for GET request"""
    response = jsonify(server_data.shopping_list)
    return response

@app.route('/shopping_list/timestamp')
@cross_origin()
def get_timestamp():
    """Get all items from shopping list in json format for GET request"""
    response = {'timestamp': server_data.shopping_list.get('shopping_list').get('timestamp')}
    return response

def _set_shopping_list(shopping_list_local: dict):
    print(request.json)
    server_data.write_server_data(shopping_list_local, request.json)
    response = {'timestamp': shopping_list_local.get('shopping_list').get('timestamp')}
    return response, 201

@app.route('/shopping_list_test')
@cross_origin()
def get_items_test():
    """Get all items from test shopping list in json format for GET request"""
    response = jsonify(server_data.shopping_list_test)
    return response

@app.route('/shopping_list_test/timestamp')
@cross_origin()
def get_timestamp_test():
    """Get all items from test shopping list in json format for GET request"""
    response = {'timestamp': server_data.shopping_list_test.get('shopping_list').get('timestamp')}
    return response


@app.route('/shopping_list', methods=['POST'])
@cross_origin()
def set_shopping_list():
    """Overwrite shopping list dictionary when POST request received"""
    returned_list = _set_shopping_list(server_data.shopping_list)
    ServerBackup(server_data.shopping_list).create_backup()
    return returned_list


@app.route('/shopping_list_test', methods=['POST'])
@cross_origin()
def set_shopping_list_test():
    """Overwrite test shopping list dictionary when POST request received"""
    returned_list = _set_shopping_list(server_data.shopping_list_test)
    ServerBackup(server_data.shopping_list_test, 'backup_test').create_backup()
    return returned_list


def load_backup():
    """Load data from backup file when server started"""
    try:
        data = ServerBackup(server_data.shopping_list).load_backup()
        server_data.shopping_list['shopping_list'] = data['shopping_list']
        data = ServerBackup(server_data.shopping_list_test, 'backup_test').load_backup()
        server_data.shopping_list_test['shopping_list'] = data['shopping_list']
    except FileNotFoundError:
        print('Backup file not found')


if __name__ == '__main__':
    load_backup()
    app.run(debug=True)
