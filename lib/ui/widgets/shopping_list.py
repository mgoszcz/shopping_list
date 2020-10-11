from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.signals.list_signals import LIST_SIGNALS


class ShoppingListTable(QTableWidget):

    def __init__(self, shopping_list: ShoppingList):
        super().__init__()
        self._shopping_list = shopping_list
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Artykuł', 'Kategoria', 'Ilość'])
        self._populate_table()

        self.cellChanged.connect(self._amount_changed)
        LIST_SIGNALS.list_changed.connect(self._populate_table)

    def _populate_table(self):
        self.setRowCount(len(self._shopping_list))
        for i, item in enumerate(self._shopping_list):
            self.setItem(i, 0, QTableWidgetItem(item.name))
            self.setItem(i, 1, QTableWidgetItem(item.category))
            self.setItem(i, 2, QTableWidgetItem(str(item.amount)))

    def _amount_changed(self):
        if self.currentColumn() == 2:
            article = self._shopping_list[self.currentRow()]
            article.amount = int(self.currentItem().text())

    def dupa(self):
        print('dupa')
        print(f'Index: {self.currentIndex()}, Row: {self.currentRow()}, Column: {self.currentColumn()}')
