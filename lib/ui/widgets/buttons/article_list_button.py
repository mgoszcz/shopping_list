"""
Module contains ArticleListButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class ArticleListButton(QPushButton):
    """
    Button for articles list dialog opening
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Lista artykułów')
