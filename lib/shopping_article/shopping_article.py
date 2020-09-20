"""
Module contains ShoppingArticle class declaration
"""
from lib.save_load.events import SAVE_NEEDED


class ShoppingArticle:
    """
    Class representing shopping article object
    """
    def __init__(self, name: str, category: str, amount: int = 1):
        self._name = name
        self._category = category
        self._amount = amount
        self._selection = 0

    def __setattr__(self, key, value):
        super(ShoppingArticle, self).__setattr__(key, value)
        SAVE_NEEDED.set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        self._category = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value: int):
        self._amount = value

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value: int):
        self._selection = value
