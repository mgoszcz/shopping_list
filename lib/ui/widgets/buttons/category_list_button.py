"""
Module contains CategoryListButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class CategoryListButton(QPushButton):
    """
    Implements push button to open category dialog
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Kategorie')
