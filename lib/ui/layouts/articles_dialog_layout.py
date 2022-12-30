"""
Module contains ArticlesDialogLayout class
"""
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton  # pylint: disable=no-name-in-module

from lib.search.article_search import ArticleSearch
from lib.shopping_list.shopping_list import NewShoppingList
from lib.ui.layouts.search_article_layout import SearchArticleLayout
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.buttons.clear_list_button import ClearListButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.tables.articles_list_table import ArticlesListTableAlphabetical


class ArticlesDialogLayout(QVBoxLayout):
    """
    Layout for articles dialog
    """

    def __init__(self, items_list: NewShoppingList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ARTICLES_DIALOG_LAYOUT)
        self._items_list = items_list
        self.articles_table = ArticlesListTableAlphabetical(self._items_list.shopping_articles_list, 2)
        self.add_button = AddButton()
        self.remove_button = RemoveButton()
        self.clear_list_button = ClearListButton()
        self.add_to_shopping_list_button = QPushButton('Dodaj do listy')
        self.search_layout = SearchArticleLayout(self._items_list.shopping_articles_list)
        buttons = QHBoxLayout()
        buttons.addWidget(self.add_to_shopping_list_button)
        buttons.addWidget(self.add_button)
        buttons.addWidget(self.remove_button)
        buttons.addWidget(self.clear_list_button)
        self.addLayout(self.search_layout)
        self.addWidget(self.articles_table)
        self.addLayout(buttons)

        self.search_layout.search_box.textChanged.connect(self.filter_articles)

    def filter_articles(self):
        """Filter articles displayed in table regarding to search string"""
        filter_text = self.search_layout.search_box.text()
        if not filter_text:
            self.articles_table.filter_articles(self._items_list.shopping_articles_list)
        else:
            self.articles_table.filter_articles(
                ArticleSearch(self._items_list.shopping_articles_list).search_by_name(filter_text))
