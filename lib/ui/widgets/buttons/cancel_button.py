"""
Module contains CancelButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class CancelButton(QPushButton):
    """
    Implementation of cancel button
    """
    def __init__(self):
        super().__init__()
        self.setText('Anuluj')
