"""
Module with functions to handle rest api on client side
"""
import requests

from lib.rest_api.db_to_json import DbToJson
from lib.rest_api.server_addr import REST_API_SERVER, SHOPPING_LIST_NAME


def save_items(interface: 'ShoppingListInterface'):
    """
    Save items to server
    :param interface: shopping list interface instance
    """
    object_to_save = DbToJson(interface).run()
    server_response = requests.post(f'{REST_API_SERVER}/{SHOPPING_LIST_NAME}', json=object_to_save)
    print(server_response)
    print(server_response.json())


def get_items() -> dict:
    """
    Get items from server
    :return: dictionary with all items
    """
    objects = requests.get(f'{REST_API_SERVER}/{SHOPPING_LIST_NAME}')
    return objects.json()
