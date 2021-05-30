"""
Module contains PrintButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class PrintButton(QPushButton):
    """
    Implementation of print button
    """
    def __init__(self):
        super().__init__()
        self.setText('Drukuj')
