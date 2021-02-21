import requests

from lib.rest_api.db_to_json import DbToJson
from lib.rest_api.server_addr import REST_API_SERVER

def add_item(name, category):
    obj = {'name': name, 'category': category}
    resp = requests.post(f'{REST_API_SERVER}/items', json=obj)
    print(resp.text)


def save_items(interface):
    obj = DbToJson(interface).run()
    ret = requests.post(f'{REST_API_SERVER}/shopping_list_test', json=obj)
    print(ret)


def get_items() -> dict:
    objects = requests.get(f'{REST_API_SERVER}/shopping_list_test')
    return objects.json()



pass
