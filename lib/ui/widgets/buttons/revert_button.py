"""
Module contains RevertButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class RevertButton(QPushButton):
    """
    Implementation of revert button
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.REVERT_BUTTON)
        self.setText('Przywróć')
