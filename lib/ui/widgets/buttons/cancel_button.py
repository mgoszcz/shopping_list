"""
Module contains CancelButton class
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class CancelButton(QPushButton):
    """
    Implementation of cancel button
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CANCEL_BUTTON)
        self.setText('Anuluj')
