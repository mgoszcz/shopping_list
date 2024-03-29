"""
Module contains buttons to move categories
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class MoveUpButton(QPushButton):
    """
    Push button to move category up
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.MOVE_UP_BUTTON)
        self.setText('\u2191')


class MoveDownButton(QPushButton):
    """
    Push button to move category down
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.MOVE_DOWN_BUTTON)
        self.setText('\u2193')


class MoveToTopButton(QPushButton):
    """
    Push button to move category to top
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.MOVE_TOP_BUTTON)
        self.setText('\u219f')


class MoveToBottomButton(QPushButton):
    """
    Push button to move category to bottom
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.MOVE_BOTTOM_BUTTON)
        self.setText('\u21a1')
