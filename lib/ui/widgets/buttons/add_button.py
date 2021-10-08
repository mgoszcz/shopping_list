"""
Add Button implementation
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class AddButton(QPushButton):
    """
    Add Button implementation
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName('add_button')
        self.setText('Dodaj')
