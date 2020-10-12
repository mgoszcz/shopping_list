
from PyQt5.QtWidgets import QComboBox

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.signals.list_signals import LIST_SIGNALS


class ArticleComboBox(QComboBox):

    def __init__(self, items_list: ShoppingArticlesList):
        super().__init__()
        self.items = items_list

        self.addItem('Dodaj...')
        self._populate_list()
        self.setEditable(True)

        self.activated.connect(self.add_article)
        LIST_SIGNALS.list_changed.connect(self._populate_list)

    def _populate_list(self):
        try:
            current_item = self.get_current_article()
        except IndexError:
            current_item = 0
        for i in reversed(range(1, self.count())):
            self.removeItem(i)
        self.addItems([x for x in self.items.print_names_and_categories()])
        if current_item in self.items and current_item != 0:
            self.setCurrentIndex(self.items.index(current_item) + 1)
        else:
            self.setCurrentIndex(1)

    def add_article(self):
        if self.currentIndex() == 0:
            dialog = AddNewArticleDialog(self.items)
            if dialog.exec_():
                self._populate_list()
                self.setCurrentIndex(self.count() - 1)
            else:
                self.setCurrentIndex(1)

    def get_current_article(self):
        if self.currentIndex() == 0:
            raise IndexError('Current index is 0')
        if self.currentIndex() < 0:
            raise IndexError('Current index is below 0')
        return self.items[self.currentIndex() - 1]
