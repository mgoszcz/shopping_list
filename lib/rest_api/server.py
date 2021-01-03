from flask import Flask, jsonify, request

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
    global shopping_list
    shopping_list = {
        'shopping_articles_list': request.json['shopping_articles_list'],
        'shopping_list': request.json['shopping_list'],
        'categories': request.json['categories'],
        'shops': request.json['shops'],
        'current_shop': request.json['current_shop']
    }
    return jsonify({'shopping_list': shopping_list}), 201


if __name__ == '__main__':
    app.run(debug=True)
