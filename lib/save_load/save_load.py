import os
import pickle
import time
from threading import Thread, Event

from lib.article_dict import ArticleDict
from lib.events import SAVE_NEEDED, AUTO_SAVE_PAUSED

MAIN_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class AutoSave(Thread):
    __save_needed = Event()
    __auto_save_paused = Event()

    def __init__(self, collection: ArticleDict):
        super(AutoSave, self).__init__()
        self._collection = collection
        self.stop = Event()

    def run(self):
        while not self.stop.is_set():
            if SAVE_NEEDED.is_set():
                print('Save needed, save data')
                SaveLoad(self._collection).save_data()
                SAVE_NEEDED.clear()
            time.sleep(5)


class SaveLoad:

    def __init__(self, articles_list, file_path=f'{MAIN_DIRECTORY}/database.dat'):
        self.file_path = file_path
        self.articles_list = articles_list

    def save_data(self):
        data = {'articles_list': self.articles_list}
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)

    def load_data(self):
        if not os.path.exists(self.file_path):
            return
        AUTO_SAVE_PAUSED.set()
        with open(self.file_path, 'rb') as f:
            content = pickle.load(f)
        for key, value in content['articles_list'].items():
            self.articles_list[key] = value
        AUTO_SAVE_PAUSED.clear()
