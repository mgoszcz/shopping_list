"""
Module contains class RemoveButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class RemoveButton(QPushButton):
    """
    Implementation of remove button
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Usuń')
