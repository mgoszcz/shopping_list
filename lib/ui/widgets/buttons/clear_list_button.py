"""
Module contains class ClearListButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class ClearListButton(QPushButton):
    """
    Implementation of push button to clear list
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Wyczyść')
