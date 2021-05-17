"""Module contains Shop class"""
from lib.save_load.events import SAVE_NEEDED
from lib.shopping_categories.category_list import CategoryList


class Shop:
    """Implementation of shop object"""
    def __init__(self, name: str, logo: str = None):
        self._name = name
        self._logo = logo
        self._category_list: CategoryList = CategoryList()

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        SAVE_NEEDED.set()

    @property
    def name(self):
        """Get name of shop"""
        return self._name

    @name.setter
    def name(self, value):
        """Set name of shop"""
        self._name = value

    @property
    def logo(self):
        """Get logo of shop"""
        return self._logo

    @logo.setter
    def logo(self, value):
        """Set logo of shop"""
        self._logo = value

    @property
    def category_list(self):
        """Get category list for shop"""
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        """Get category list for shop"""
        self._category_list = value
