"""
Module contains class EditButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class EditButton(QPushButton):
    """
    Implementation of edit push button
    """
    def __init__(self):
        super().__init__()
        self.setText('Edytuj')
