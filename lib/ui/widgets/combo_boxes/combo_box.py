"""
Module contains class ArticleComboBox
"""
from typing import Optional

from PyQt5.QtWidgets import QComboBox  # pylint: disable=no-name-in-module

from lib.search.article_search import ArticleSearch
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.list_signals import LIST_SIGNALS


class ArticleComboBox(QComboBox):
    """
    Implementation of combo box with articles from articles list
    """
    def __init__(self, items_list: ShoppingArticlesList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ARTICLE_COMBO_BOX)
        self._items = items_list
        self._displayed_items = items_list
        self.combobox_items = []

        self.addItem('Dodaj...')
        self._populate_list()
        self.setEditable(True)

        self.activated.connect(self.add_article)
        self.currentTextChanged.connect(self.filter_article)
        LIST_SIGNALS.list_changed.connect(self._populate_list)

    def _populate_list(self):
        try:
            current_item = self.get_current_article()
        except (IndexError, AttributeError):
            current_item = 0
        self.combobox_items = []
        for i in reversed(range(1, self.count())):
            self.removeItem(i)
        for item in sorted(self._displayed_items, key=lambda x: x.name):
            self.combobox_items.append(item.name)
            self.addItem(f'{item.name} - {item.category}')
        # if current_item in self._displayed_items and current_item != 0:
        #     self.setCurrentIndex(self.combobox_items.index(current_item.name) + 1)
        # else:
        #     self.setCurrentIndex(1)

    def add_article(self):
        """
        Method invoked when selected item changed, if current index is 0 then add article dialog will be opened,
        otherwise it will do nothing
        """
        if self.currentIndex() == 0:
            dialog = AddNewArticleDialog(self._items)
            if dialog.exec_():
                self._displayed_items = self._items
                self._populate_list()
                index = self.combobox_items.index(dialog.article_name)
                self.setCurrentIndex(index + 1)
            else:
                self.setCurrentIndex(1)

    def get_current_article(self) -> Optional[ShoppingArticle]:
        """
        Get article object for selected article name
        """
        if self.currentIndex() == 0:
            raise IndexError('Current index is 0')
        if self.currentIndex() < 0:
            raise IndexError('Current index is below 0')
        if not self.currentIndex() > len(self.combobox_items):
            return self._items.get_article_by_name(self.combobox_items[self.currentIndex() - 1])
        return None

    def filter_article(self):
        current_text = self.currentText()
        if not current_text:
            self._displayed_items = self._items
        else:
            print('a')
            self._displayed_items = ArticleSearch(self._items).search_by_name(current_text)
        self._populate_list()
