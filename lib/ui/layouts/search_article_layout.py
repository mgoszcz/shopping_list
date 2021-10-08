"""Module contains SearchArticleLayout class"""
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit  # pylint: disable=no-name-in-module

from lib.search.article_search import ArticleSearch
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.object_names.object_names import ObjectNames


class SearchArticleLayout(QVBoxLayout):
    """Class holds implementation of search article entry"""
    def __init__(self, shopping_articles_list: ShoppingArticlesList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.SEARCH_ARTICLES_LAYOUT)
        self._articles = shopping_articles_list
        self.search = ArticleSearch(self._articles)
        self.search_box = QLineEdit()
        self.addWidget(self.search_box)
