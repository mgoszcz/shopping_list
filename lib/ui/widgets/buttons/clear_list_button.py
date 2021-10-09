"""
Module contains class ClearListButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class ClearListButton(QPushButton):
    """
    Implementation of push button to clear list
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CLEAR_LIST_BUTTON)
        self.setText('Wyczyść')
