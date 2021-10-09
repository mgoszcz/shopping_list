"""
Module contains class EditButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class EditButton(QPushButton):
    """
    Implementation of edit push button
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.EDIT_BUTTON)
        self.setText('Edytuj')
