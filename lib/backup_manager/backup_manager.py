import os
import pickle
import time
from typing import List

from lib.save_load.events import AUTO_SAVE_PAUSED, SAVE_NEEDED
from lib.shop.shops_list import ShopsList
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.shopping_categories.category_list import CategoryList
from lib.ui.signals.list_signals import LIST_SIGNALS

AUTO_BACKUP_PREFIX = '_auto_backup_'


class BackupManager:

    def __init__(self, interface: 'ShoppingListInterface', file_directory=f'backups'):
        self._interface = interface
        self.file_directory = file_directory
        self.backups_list = []

        self._cleanup_backup_folder()

        if not os.path.exists(self.file_directory):
            os.mkdir(self.file_directory)

    def _get_auto_file_path(self) -> str:
        timestamp = time.strftime("%d_%m_%Y__%H_%M_%S", time.localtime())
        filename = f'{AUTO_BACKUP_PREFIX}{timestamp}'
        return os.path.join(self.file_directory, filename)

    def _get_backup_files(self) -> List[str]:
        return [file for file in os.listdir(self.file_directory) if
                os.path.isfile(os.path.join(self.file_directory, file))]

    def _cleanup_backup_folder(self):
        if os.path.exists(self.file_directory):
            for file_name in self._get_backup_files():
                if file_name.startswith(AUTO_BACKUP_PREFIX):
                    os.remove(os.path.join(self.file_directory, file_name))

    def _populate_backups_list(self):
        if os.path.exists(self.file_directory):
            for file_name in self._get_backup_files():
                self.backups_list.append(file_name)

    def _clear_interface(self):
        self._interface.categories = CategoryList()
        self._interface.shops = ShopsList(self._interface.categories)
        self._interface.shopping_articles = ShoppingArticlesList(self._interface.categories, self._interface.shops)
        self._interface.shopping_list = ShoppingList(self._interface.shopping_articles, self._interface.shops)

    def create_backup(self, auto: bool = False):
        data = {'shops': self._interface.shops, 'categories': self._interface.categories,
                'shopping_articles': self._interface.shopping_articles, 'shopping_list': self._interface.shopping_list}
        if auto:
            file_path = self._get_auto_file_path()
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
        self.backups_list.append(file_path.split(os.sep)[-1])

    def restore_backup(self, backup_name: str):
        if not os.path.exists(os.path.join(self.file_directory, backup_name)):
            raise AttributeError(f'Backup {backup_name} does not exist')
        AUTO_SAVE_PAUSED.set()
        with open(os.path.join(self.file_directory, backup_name), 'rb') as f:
            content = pickle.load(f)
        # self._clear_interface()
        self._interface.shops.clear()
        self._interface.shops.extend(content['shops'])
        self._interface.shops.selected_shop = content['shops'].selected_shop
        self._interface.categories.clear()
        self._interface.categories.extend(content['categories'])
        self._interface.shopping_articles.clear()
        self._interface.shopping_articles.extend(content['shopping_articles'])
        self._interface.shopping_list.clear()
        self._interface.shopping_list.extend(content['shopping_list'])
        self._interface.shopping_list.sort_by_shop()
        AUTO_SAVE_PAUSED.clear()
        SAVE_NEEDED.set()

    def remove_backup(self, backup_name: str):
        backup_path = os.path.join(self.file_directory, backup_name)
        if not os.path.exists(backup_path):
            raise AttributeError(f'Backup {backup_name} does not exist')
        os.remove(backup_path)
        self.backups_list.remove(backup_name)