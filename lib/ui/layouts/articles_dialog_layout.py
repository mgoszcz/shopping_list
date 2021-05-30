"""
Module contains ArticlesDialogLayout class
"""
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout  # pylint: disable=no-name-in-module

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.buttons.clear_list_button import ClearListButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.tables.articles_list_table import ArticlesListTableAlphabetical


class ArticlesDialogLayout(QVBoxLayout):
    """
    Layout for articles dialog
    """
    def __init__(self, items_list: ShoppingArticlesList):
        super().__init__()
        self._items_list = items_list
        self.articles_table = ArticlesListTableAlphabetical(self._items_list, 2)
        self.add_button = AddButton()
        self.remove_button = RemoveButton()
        self.clear_list_button = ClearListButton()
        buttons = QHBoxLayout()
        buttons.addWidget(self.add_button)
        buttons.addWidget(self.remove_button)
        buttons.addWidget(self.clear_list_button)
        self.addWidget(self.articles_table)
        self.addLayout(buttons)
