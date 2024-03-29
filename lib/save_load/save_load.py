"""Module contains SaveLoad and AutoSave class"""
import base64
import os
import time
from threading import Thread, Event
from typing import TYPE_CHECKING

from lib.file_manager.file_object import FileObject
from lib.rest_api.client import save_items, get_items
from lib.save_load.events import AUTO_SAVE_PAUSED, SAVE_NEEDED
from lib.shop.shop import Shop
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_list.shopping_list_item import ShoppingListItem
from resources.paths.paths import SHOPS_ICONS_PATH

if TYPE_CHECKING:
    from lib.shopping_list_interface import ShoppingListInterface

MAIN_DIRECTORY = os.path.join('..', os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class SaveLoad:
    """Class responsible for save and load handling"""

    def __init__(self, interface: 'ShoppingListInterface'):
        self._interface = interface

    def _load_articles_from_server(self, items: dict):
        if not items:
            return
        if items.get('shopping_articles_list'):
            for article in items.get('shopping_articles_list'):
                new_article = ShoppingArticle(name=article.get('name'), category=article.get('category'),
                                              amount=article.get('amount'))
                new_article.selection = article.get('selection')
                self._interface.shopping_articles.append(new_article)

    def _load_shopping_list_from_server(self, items: dict):
        if not items:
            return
        if items.get('shopping_list'):
            for item in items.get('shopping_list'):
                if isinstance(item, dict):
                    # New format of data on server - dictionary
                    article = self._interface.shopping_articles.get_article_by_name(item.get('article_name'))
                    self._interface.shopping_list.append(
                        ShoppingListItem(article, item.get('amount'), item.get('checked')))
                elif isinstance(item, str):
                    # Old format of data no server - string with article name
                    article = self._interface.shopping_articles.get_article_by_name(item)
                    self._interface.shopping_list.append(ShoppingListItem(article))
                else:
                    raise RuntimeError('Invalid shopping list data from server')

    def _load_shops_from_server(self, items: dict):
        if not items:
            return
        if items.get('shops'):
            for shop in items.get('shops'):
                new_shop = Shop(name=shop.get('name'), logo=shop.get('logo'))
                new_shop.category_list.custom_sort = True
                for category in shop.get('category_list'):
                    new_shop.category_list.append(category)
                self._interface.shops.append(new_shop)

    @staticmethod
    def _load_shops_icons_from_server(items: dict):
        if not items:
            return
        if items.get('shops_icons'):
            if not os.path.isdir(SHOPS_ICONS_PATH):
                os.mkdir(SHOPS_ICONS_PATH)
            for filename, image in items.get('shops_icons').items():
                icon_file = FileObject(os.path.join(SHOPS_ICONS_PATH, filename))
                if icon_file.exists():
                    icon_file.remove()
                with open(icon_file.file_path, 'wb') as decodeit:
                    decodeit.write(base64.b64decode((bytes(image, 'utf-8'))))

    def save_data_to_server(self):
        """Save data to rest api server"""
        save_items(self._interface)
        self._interface.backup_manager.create_backup(auto=True)

    def load_data_from_server(self):
        """Load data from REST API server"""
        AUTO_SAVE_PAUSED.set()
        data_from_server = get_items().get('shopping_list')
        self._load_articles_from_server(data_from_server)
        self._load_shopping_list_from_server(data_from_server)
        self._load_shops_from_server(data_from_server)
        self._load_shops_icons_from_server(data_from_server)
        if not data_from_server:
            return
        if data_from_server.get('current_shop'):
            shop = self._interface.shops.get_shop_by_name(data_from_server.get('current_shop'))
            self._interface.shops.selected_shop = shop
        else:
            self._interface.shops.selected_shop = None
        AUTO_SAVE_PAUSED.clear()


class AutoSave(Thread):
    """Class responsible for auto save running in separate thread"""

    def __init__(self, save_load: SaveLoad):
        super().__init__()
        self._save_load = save_load
        self.stop = Event()

    def run(self):
        """Run thread with auto save"""
        while not self.stop.is_set():
            if SAVE_NEEDED.is_set():
                print('Save needed, save data')
                self._save_load.save_data_to_server()
                SAVE_NEEDED.clear()
            time.sleep(5)
