"""
Module contains class BackupManager
"""
import os
import pickle
import time
from typing import List

from lib.save_load.events import AUTO_SAVE_PAUSED, SAVE_NEEDED
from lib.shop.shops_list import ShopsList
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.shopping_categories.category_list import CategoryList

AUTO_BACKUP_PREFIX = '_auto_backup_'


class BackupManager:
    """
    Implementation of backup manager responsible for creating, restoring and removing backups
    It creates automatic and on demand backups, all backups are kept in backups_list
    It populates backups list on initialization basing on backup files
    """
    def __init__(self, interface: 'ShoppingListInterface', file_directory='backups'):
        self._interface = interface
        self.file_directory = file_directory
        self.backups_list = []

        self._cleanup_backup_folder()
        self._populate_backups_list()

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
                self._add_backup_to_list(file_name)

    def _clear_interface(self):
        self._interface.categories = CategoryList()
        self._interface.shops = ShopsList(self._interface.categories)
        self._interface.shopping_articles = ShoppingArticlesList(self._interface.categories, self._interface.shops)
        self._interface.shopping_list = ShoppingList(self._interface.shopping_articles, self._interface.shops)

    def _add_backup_to_list(self, backup_name: str):
        if backup_name.lower() in [bkp.lower() for bkp in self.backups_list]:
            raise AttributeError(f'Backup {backup_name} is already on list')
        if backup_name.startswith(AUTO_BACKUP_PREFIX):
            self.backups_list.append(backup_name)
        else:
            index = next((i for i, value in enumerate(self.backups_list) if value.startswith(AUTO_BACKUP_PREFIX)), None)
            if index:
                self.backups_list.insert(index, backup_name)
            else:
                self.backups_list.append(backup_name)

    def create_backup(self, auto: bool = False, file_name: str = None):
        """
        Create backup - automatic or on demand depends on parameters
        :param auto: determine if creating auto backup or user backup
        :param file_name: name of backup file (for user backups only)
        """
        data = {'shops': self._interface.shops, 'categories': self._interface.categories,
                'shopping_articles': self._interface.shopping_articles, 'shopping_list': self._interface.shopping_list}
        if auto:
            file_path = self._get_auto_file_path()
        else:
            if not file_name:
                raise AttributeError('Backup file name cannot be empty')
            if file_name.startswith(AUTO_BACKUP_PREFIX):
                raise AttributeError(f'Backup file name cannot start with string: {AUTO_BACKUP_PREFIX}')
            file_path = os.path.join(self.file_directory, file_name)
        with open(file_path, 'wb') as backup_file:
            pickle.dump(data, backup_file)
        self._add_backup_to_list(file_path.split(os.sep)[-1])

    def restore_backup(self, backup_name: str):
        """
        Restore backup from backup file
        :param backup_name: name of backup file to be restored
        """
        if not os.path.exists(os.path.join(self.file_directory, backup_name)):
            raise AttributeError(f'Backup {backup_name} does not exist')
        AUTO_SAVE_PAUSED.set()
        with open(os.path.join(self.file_directory, backup_name), 'rb') as backup_file:
            content = pickle.load(backup_file)
        self._interface.shops.clear()
        self._interface.shops.extend(content['shops'])
        self._interface.shops.selected_shop = content['shops'].selected_shop
        self._interface.shopping_articles.clear()
        self._interface.shopping_articles.extend(content['shopping_articles'])
        self._interface.categories.extend(content['categories'])
        self._interface.shopping_list.clear()
        self._interface.shopping_list.extend(content['shopping_list'])
        self._interface.shopping_list.sort_by_shop()
        AUTO_SAVE_PAUSED.clear()
        SAVE_NEEDED.set()

    def remove_backup(self, backup_name: str):
        """
        Remove backup - removes file and list item
        :param backup_name: name of file to be removed
        """
        backup_path = os.path.join(self.file_directory, backup_name)
        if not os.path.exists(backup_path):
            raise AttributeError(f'Backup {backup_name} does not exist')
        os.remove(backup_path)
        self.backups_list.remove(backup_name)
