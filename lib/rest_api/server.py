"""Module contains REST api server implementation"""
from flask import Flask, jsonify, request

from lib.rest_api.server_backup import ServerBackup

app = Flask(__name__)

shopping_list = dict()
shopping_list_test = dict()


@app.route('/')
def index():
    """home page"""
    return "INDEX"


@app.route('/shopping_list')
def get_items():
    """Get all items from shopping list in json format for GET request"""
    return jsonify(shopping_list)


def _set_shopping_list(shopping_list_local: dict):
    current_list = {
        'shopping_articles_list': request.json['shopping_articles_list'],
        'shopping_list': request.json['shopping_list'],
        'categories': request.json['categories'],
        'shops': request.json['shops'],
        'current_shop': request.json['current_shop']
    }
    shopping_list_local['shopping_list'] = current_list
    return jsonify(shopping_list_local), 201


@app.route('/shopping_list_test')
def get_items_test():
    """Get all items from test shopping list in json format for GET request"""
    return jsonify(shopping_list_test)


@app.route('/shopping_list', methods=['POST'])
def set_shopping_list():
    """Overwrite shopping list dictionary when POST request received"""
    returned_list = _set_shopping_list(shopping_list)
    ServerBackup(shopping_list).create_backup()
    return returned_list


@app.route('/shopping_list_test', methods=['POST'])
def set_shopping_list_test():
    """Overwrite test shopping list dictionary when POST request received"""
    returned_list = _set_shopping_list(shopping_list_test)
    ServerBackup(shopping_list_test, 'backup_test').create_backup()
    return returned_list


def load_backup():
    """Load data from backup file when server started"""
    try:
        data = ServerBackup(shopping_list).load_backup()
        shopping_list['shopping_list'] = data['shopping_list']
        data = ServerBackup(shopping_list_test, 'backup_test').load_backup()
        shopping_list_test['shopping_list'] = data['shopping_list']
    except FileNotFoundError:
        print('Backup file not found')


if __name__ == '__main__':
    load_backup()
    app.run(debug=True)
