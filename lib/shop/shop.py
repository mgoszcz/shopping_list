from lib.save_load.events import SAVE_NEEDED
from lib.shopping_categories.category_list import CategoryList


class Shop:

    def __init__(self, name: str, logo: str = None):
        self._name = name
        self._logo = logo
        self._category_list: CategoryList = CategoryList()

    def __setattr__(self, key, value):
        super(Shop, self).__setattr__(key, value)
        SAVE_NEEDED.set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value

    @property
    def category_list(self):
        return self._category_list
