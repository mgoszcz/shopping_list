import os
import pickle
import time
from threading import Thread, Event
from typing import TYPE_CHECKING

from lib.save_load.events import AUTO_SAVE_PAUSED, SAVE_NEEDED

if TYPE_CHECKING:
    from lib.shopping_list_interface import ShoppingListInterface

MAIN_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class SaveLoad:

    def __init__(self, interface: 'ShoppingListInterface', file_path=f'{MAIN_DIRECTORY}/database.dat'):
        self.file_path = file_path
        self._interface = interface

    def save_data(self):
        data = {'shops': self._interface.shops, 'categories': self._interface.categories,
                'shopping_articles': self._interface.shopping_articles, 'shopping_list': self._interface.shopping_list}
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)

    def load_data(self):
        if not os.path.exists(self.file_path):
            return
        AUTO_SAVE_PAUSED.set()
        with open(self.file_path, 'rb') as f:
            content = pickle.load(f)
        self._interface.shops = content['shops']
        self._interface.categories = content['categories']
        self._interface.shopping_articles = content['shopping_articles']
        self._interface.shopping_list = content['shopping_list']
        self._interface.shopping_list.sort_by_shop()
        AUTO_SAVE_PAUSED.clear()


class AutoSave(Thread):

    def __init__(self, save_load: SaveLoad):
        super(AutoSave, self).__init__()
        self._save_load = save_load
        self.stop = Event()

    def run(self):
        while not self.stop.is_set():
            if SAVE_NEEDED.is_set():
                print('Save needed, save data')
                self._save_load.save_data()
                SAVE_NEEDED.clear()
            time.sleep(5)
