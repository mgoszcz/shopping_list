from flask import Flask, jsonify, request

from lib.rest_api.server_backup import ServerBackup

app = Flask(__name__)

shopping_list = dict()


@app.route('/')
def index():
    return "INDEX"


@app.route('/shopping_list')
def get_items():
    return jsonify(shopping_list)


@app.route('/shopping_list', methods=['POST'])
def set_shopping_list():
    current_list = {
        'shopping_articles_list': request.json['shopping_articles_list'],
        'shopping_list': request.json['shopping_list'],
        'categories': request.json['categories'],
        'shops': request.json['shops'],
        'current_shop': request.json['current_shop']
    }
    shopping_list['shopping_list'] = current_list
    ServerBackup(shopping_list).create_backup()
    return jsonify(shopping_list), 201


def load_backup():
    try:
        data = ServerBackup(shopping_list).load_backup()
        shopping_list['shopping_list'] = data['shopping_list']
    except FileNotFoundError:
        print('Backup file not found')

if __name__ == '__main__':
    load_backup()
    app.run(debug=True)
