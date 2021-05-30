"""
Module contains class RemoveButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class RemoveButton(QPushButton):
    """
    Implementation of remove button
    """
    def __init__(self):
        super().__init__()
        self.setText('Usuń')
