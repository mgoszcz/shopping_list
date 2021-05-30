"""
Module contains class ClearListButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class ClearListButton(QPushButton):
    """
    Implementation of push button to clear list
    """
    def __init__(self):
        super().__init__()
        self.setText('Wyczyść')
