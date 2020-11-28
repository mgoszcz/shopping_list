
from PyQt5.QtWidgets import QComboBox

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.signals.list_signals import LIST_SIGNALS


class ArticleComboBox(QComboBox):

    def __init__(self, items_list: ShoppingArticlesList):
        super().__init__()
        self._items = items_list
        self.combobox_items = []

        self.addItem('Dodaj...')
        self._populate_list()
        self.setEditable(True)

        self.activated.connect(self.add_article)
        LIST_SIGNALS.list_changed.connect(self._populate_list)

    def _populate_list(self):
        self.combobox_items = []
        try:
            current_item = self.get_current_article()
        except IndexError:
            current_item = 0
        for i in reversed(range(1, self.count())):
            self.removeItem(i)
        for item in sorted(self._items, key=lambda x: x.name):
            self.combobox_items.append(item.name)
            self.addItem(f'{item.name} - {item.category}')
        if current_item in self._items and current_item != 0:
            self.setCurrentIndex(self._items.index(current_item) + 1)
        else:
            self.setCurrentIndex(1)

    def add_article(self):
        if self.currentIndex() == 0:
            dialog = AddNewArticleDialog(self._items)
            if dialog.exec_():
                self._populate_list()
                index = self.combobox_items.index(dialog.article_name)
                self.setCurrentIndex(index + 1)
            else:
                self.setCurrentIndex(1)

    def get_current_article(self):
        if self.currentIndex() == 0:
            raise IndexError('Current index is 0')
        if self.currentIndex() < 0:
            raise IndexError('Current index is below 0')
        return self._items.get_article_by_name(self.combobox_items[self.currentIndex() - 1])
