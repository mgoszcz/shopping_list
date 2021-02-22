"""
Add Button implementation
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class AddButton(QPushButton):
    """
    Add Button implementation
    """
    def __init__(self):
        super().__init__()
        self.setText('Dodaj')
