"""
Module contains ArticleListButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class ArticleListButton(QPushButton):
    """
    Button for articles list dialog opening
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ARTICLES_LIST_BUTTON)
        self.setText('Lista artykułów')
