"""
Module contains ShoppingArticle class declaration
"""
# pylint: disable=duplicate-code
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
        super().__setattr__(key, value)
        SAVE_NEEDED.set()

    @property
    def name(self):
        """Get name of article"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Set name of article"""
        self._name = value

    @property
    def category(self):
        """Get category of article"""
        return self._category

    @category.setter
    def category(self, value: str):
        """Set category of article"""
        self._category = value

    @property
    def amount(self):
        """Get amount of article"""
        return self._amount

    @amount.setter
    def amount(self, value: int):
        """Set amount of article"""
        self._amount = value

    @property
    def selection(self):
        """Get selection value of article"""
        return self._selection

    @selection.setter
    def selection(self, value: int):
        """Set selection value of article"""
        self._selection = value
