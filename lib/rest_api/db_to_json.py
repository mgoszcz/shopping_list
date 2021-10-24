"""
Module contains class DbToJson
"""
import base64
from typing import List, Union
import os

from lib.shop.shop import Shop


class DbToJson:
    """
    Implementation of translator from DB format to Json format
    """

    def __init__(self, interface: 'ShoppingListInterface'):
        self.interface = interface

    def _get_articles_list(self) -> List[dict]:
        articles_list = []
        for article in self.interface.shopping_articles:
            articles_list.append({'name': article.name, 'category': article.category, 'amount': article.amount,
                                  'selection': article.selection})
        return articles_list

    def _get_shopping_list(self) -> List[str]:
        shopping_list = []
        for article in self.interface.shopping_list:
            shopping_list.append(article.name)
        return shopping_list

    def _get_categories(self) -> List[str]:
        categories_list = []
        for category in self.interface.categories:
            categories_list.append(category)
        return categories_list

    def _get_shops(self) -> List[dict]:
        shops_list = []
        for shop in self.interface.shops:
            shops_list.append({'name': shop.name, 'logo': shop.logo, 'category_list': shop.category_list})
        return shops_list

    def _get_current_shop(self) -> Union[Shop, None]:
        if self.interface.shops.selected_shop:
            return self.interface.shops.selected_shop.name
        return None

    def _get_shops_icons(self):
        images_paths = [f for f in os.listdir('resources/icons/shops') if
                        os.path.isfile(os.path.join('resources/icons/shops', f))]
        icons = {}
        for image in images_paths:
            if os.path.splitext(image)[1] not in ('.png', '.jpg', '.bmp'):
                continue
            with open(f'resources/icons/shops/{image}', "rb") as image2string:
                converted_string = str(base64.b64encode(image2string.read()), 'utf-8')
            icons[image] = converted_string
        return icons

    def run(self) -> dict:
        """
        Convert db to dictionary - used for json
        :return: dictionary with all data
        """
        json_dict = dict()
        json_dict['shopping_articles_list'] = self._get_articles_list()
        json_dict['shopping_list'] = self._get_shopping_list()
        json_dict['categories'] = self._get_categories()
        json_dict['shops'] = self._get_shops()
        json_dict['current_shop'] = self._get_current_shop()
        json_dict['shops_icons'] = self._get_shops_icons()
        return json_dict
