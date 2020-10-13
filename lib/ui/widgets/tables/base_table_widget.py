from typing import Union

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from lib.shopping_article.shopping_article import ShoppingArticle
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

        self.cellChanged.connect(self._cell_changed)
        LIST_SIGNALS.list_changed.connect(self.populate_table)

    def _items_modifier(self):
        return self._items_list

    @staticmethod
    def _get_item_by_column(article: ShoppingArticle, column: int):
        return [article.name, article.category, article.amount][column]

    def populate_table(self):
        modified_list = self._items_modifier()
        self.setRowCount(len(modified_list))
        for row, item in enumerate(modified_list):
            for column, value in zip(range(self._columns_count), [item.name, item.category, item.amount]):
                self.setItem(row, column, QTableWidgetItem(str(value)))

    def _action_if_existing_article(self):
        pass

    def _action_if_non_existing_article(self):
        pass

    def _amount_changed(self, article: ShoppingArticle, new_value: str):
        raise NotImplementedError

    def _name_change(self, article: ShoppingArticle, new_value: str):
        print(article.name)
        try:
            self._items_list.get_article_by_name(new_value)
            # TODO: dialog
            print('Artykuł juz jest na liscie!!')
            return False
        except AttributeError:
            if isinstance(self._items_list, ShoppingList):
                if self._action_if_existing_article:
                    return True
            if self._action_if_non_existing_article:
                return True
            return False

    def _category_change(self, article: ShoppingArticle, new_value: str):
        # TODO: odswiezanie list po zmianie kategorii
        raise NotImplementedError

    def _cell_changed(self):
        current_column = self.currentColumn()
        current_row = self.currentRow()
        article = self._items_modifier()[current_row]
        new_value = self.item(current_row, current_column).text()
        if new_value == self._get_item_by_column(article, current_column):
            return
        if current_column == 0:
            if self._name_change(article, new_value):
                return
        elif current_column == 1:
            if self._category_change(article, new_value):
                return
        elif current_column == 2:
            if self._amount_changed(article, new_value):
                return
        else:
            raise RuntimeError(f'Invalid column number {self.currentColumn()}')
        self.setItem(current_row, current_column,
                     QTableWidgetItem(self._get_item_by_column(article, current_column)))
