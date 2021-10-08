"""
Module contains class ArticleComboBox
"""
from typing import Optional

from PyQt5.QtWidgets import QComboBox  # pylint: disable=no-name-in-module

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.signals.list_signals import LIST_SIGNALS


class ArticleComboBox(QComboBox):
    """
    Implementation of combo box with articles from articles list
    """
    def __init__(self, items_list: ShoppingArticlesList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._items = items_list
        self.combobox_items = []

        self.addItem('Dodaj...')
        self._populate_list()
        self.setEditable(True)

        self.activated.connect(self.add_article)
        LIST_SIGNALS.list_changed.connect(self._populate_list)

    def _populate_list(self):
        try:
            current_item = self.get_current_article()
        except (IndexError, AttributeError):
            current_item = 0
        self.combobox_items = []
        for i in reversed(range(1, self.count())):
            self.removeItem(i)
        for item in sorted(self._items, key=lambda x: x.name):
            self.combobox_items.append(item.name)
            self.addItem(f'{item.name} - {item.category}')
        if current_item in self._items and current_item != 0:
            self.setCurrentIndex(self.combobox_items.index(current_item.name) + 1)
        else:
            self.setCurrentIndex(1)

    def add_article(self):
        """
        Method invoked when selected item changed, if current index is 0 then add article dialog will be opened,
        otherwise it will do nothing
        """
        if self.currentIndex() == 0:
            dialog = AddNewArticleDialog(self._items)
            if dialog.exec_():
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
