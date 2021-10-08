"""
Module contains CategoryListButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class CategoryListButton(QPushButton):
    """
    Implements push button to open category dialog
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CATEGORY_LIST_BUTTON)
        self.setText('Kategorie')
