from typing import Union

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.signals.list_signals import LIST_SIGNALS


class BaseTableWidget(QTableWidget):
    def __init__(self, items_list: Union[ShoppingList, ShoppingArticlesList], columns_count: int):
        super().__init__()
        self._items_list = items_list
        self._columns_count = columns_count
        self.setColumnCount(self._columns_count)
        self.setHorizontalHeaderLabels(['Artykuł', 'Kategoria', 'Ilość'][:self._columns_count])
        self.populate_table()

        self.cellChanged.connect(self._amount_changed)
        LIST_SIGNALS.list_changed.connect(self.populate_table)

    def _items_modifier(self):
        return self._items_list

    def populate_table(self):
        modified_list = self._items_modifier()
        self.setRowCount(len(modified_list))
        for row, item in enumerate(modified_list):
            for column, value in zip(range(self._columns_count), [item.name, item.category, item.amount]):
                self.setItem(row, column, QTableWidgetItem(value))

    def _amount_changed(self):
        pass
