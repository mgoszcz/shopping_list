"""
Module with functions to handle rest api on client side
"""
import requests

from lib.rest_api.db_to_json import DbToJson
from lib.rest_api.server_addr import REST_API_SERVER


def save_items(interface: 'ShoppingListInterface'):
    """
    Save items to server
    :param interface: shopping list interface instance
    """
    obj = DbToJson(interface).run()
    ret = requests.post(f'{REST_API_SERVER}/shopping_list_test', json=obj)
    print(ret)


def get_items() -> dict:
    """
    Get items from server
    :return: dictionary with all items
    """
    objects = requests.get(f'{REST_API_SERVER}/shopping_list_test')
    return objects.json()
