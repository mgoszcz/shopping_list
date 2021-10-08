"""
Module contains BaseTableWidget class
"""
from typing import Union

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem  # pylint: disable=no-name-in-module

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.dialogs.error_dialog import ErrorDialog
from lib.ui.signals.list_signals import LIST_SIGNALS


class BaseTableWidget(QTableWidget):
    """
    Implementation of base table widget - all common properties and actions, interface implementation
    """
    def __init__(self, items_list: Union[ShoppingList, ShoppingArticlesList], columns_count: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items_list = items_list
        self._columns_count = columns_count
        self.setColumnCount(self._columns_count)
        self.setHorizontalHeaderLabels(['Artykuł', 'Kategoria', 'Ilość'][:self._columns_count])
        self.populate_table()

        self.cellChanged.connect(self._cell_changed)
        LIST_SIGNALS.list_changed.connect(self.populate_table)

    def _items_modifier(self):
        return self.items_list

    def _color_unordered_rows(self):
        pass

    @staticmethod
    def _get_item_by_column(article: ShoppingArticle, column: int):
        return [article.name, article.category, article.amount][column]

    def populate_table(self):
        """
        Populate items with table, if needed modify items and color cells
        """
        self.blockSignals(True)
        modified_list = self._items_modifier()
        self.setRowCount(len(modified_list))
        for row, item in enumerate(modified_list):
            for column, value in zip(range(self._columns_count), [item.name, item.category, item.amount]):
                self.setItem(row, column, QTableWidgetItem(str(value)))
        self._color_unordered_rows()
        self.blockSignals(False)

    def _action_if_existing_article(self, article: ShoppingArticle, shopping_list: ShoppingList, new_value: str):
        raise NotImplementedError

    def _action_if_non_existing_article(self, article: ShoppingArticle, shopping_list: ShoppingList, new_value: str):
        raise NotImplementedError

    def _amount_changed(self, article: ShoppingArticle, new_value: str):
        raise NotImplementedError

    def _name_change(self, article: ShoppingArticle, new_value: str):
        try:
            self.items_list.get_article_by_name(new_value)
            ErrorDialog(f'Artykuł {new_value} juz jest na liscie').exec_()
            return False
        except AttributeError:
            if isinstance(self.items_list, ShoppingList):
                if self._action_if_existing_article(article, self.items_list, new_value):
                    return True
            if self._action_if_non_existing_article(article, self.items_list, new_value):
                return True
            return False

    def _category_change(self, article: ShoppingArticle, new_value: str):
        raise NotImplementedError

    def _cell_changed(self):
        current_column = self.currentColumn()
        current_row = self.currentRow()
        article = self._items_modifier()[current_row]
        new_value = self.item(current_row, current_column).text()
        if new_value == self._get_item_by_column(article, current_column):
            return
        self.blockSignals(True)
        success = False
        if current_column == 0:
            if self._name_change(article, new_value):
                success = True
        elif current_column == 1:
            if self._category_change(article, new_value):
                success = True
        elif current_column == 2:
            if self._amount_changed(article, new_value):
                success = True
        else:
            raise RuntimeError(f'Invalid column number {self.currentColumn()}')
        if not success:
            self.setItem(current_row, current_column,
                         QTableWidgetItem(self._get_item_by_column(article, current_column)))
        self.blockSignals(False)
        if success:
            print(1)
            LIST_SIGNALS.list_changed.emit()
            self.populate_table()
