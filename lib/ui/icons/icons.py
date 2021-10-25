"""
Module with icons
"""

from PyQt5.QtGui import QIcon  # pylint: disable=no-name-in-module


class Icon:
    """Parent class with implementation"""
    PATH = ''

    @classmethod
    def q_icon(cls):
        """Return QIcon object with path specified"""
        return QIcon(cls.PATH)


class ShoppingListIcon(Icon):
    """
    Main Application Icon
    """
    PATH = 'resources/icons/shopping_list_icon.png'


class ErrorIcon(Icon):
    """
    Error Icon
    """
    PATH = 'resources/icons/error_icon.png'


class QuestionIcon(Icon):
    """
    Question Icon
    """
    PATH = 'resources/icons/question_icon.png'


class AddIcon(Icon):
    """Add icon"""
    PATH = 'resources/icons/add.png'


class RemoveIcon(Icon):
    """Remove icon"""
    PATH = 'resources/icons/remove.png'


class EditIcon(Icon):
    """Edit icon"""
    PATH = 'resources/icons/edit.png'
