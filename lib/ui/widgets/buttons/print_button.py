"""
Module contains PrintButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class PrintButton(QPushButton):
    """
    Implementation of print button
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.PRINT_BUTTON)
        self.setText('Drukuj')
