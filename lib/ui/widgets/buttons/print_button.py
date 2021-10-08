"""
Module contains PrintButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class PrintButton(QPushButton):
    """
    Implementation of print button
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Drukuj')
