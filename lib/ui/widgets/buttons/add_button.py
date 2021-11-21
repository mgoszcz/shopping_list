"""
Add Button implementation
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.icons.icons import AddIcon
from lib.ui.object_names.object_names import ObjectNames


class AddButton(QPushButton):
    """
    Add Button implementation
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_BUTTON)
        self.setText('Dodaj')


class AddButtonWithIcon(QPushButton):
    """
    Add Button implementation
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_BUTTON_WITH_ICON)
        self.setIcon(AddIcon.q_icon())
        self.setToolTip('Dodaj')
