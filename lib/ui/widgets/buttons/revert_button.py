"""
Module contains RevertButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class RevertButton(QPushButton):
    """
    Implementation of revert button
    """
    def __init__(self):
        super().__init__()
        self.setText('Przywróć')
