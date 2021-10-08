"""
Module contains CancelButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class CancelButton(QPushButton):
    """
    Implementation of cancel button
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Anuluj')
