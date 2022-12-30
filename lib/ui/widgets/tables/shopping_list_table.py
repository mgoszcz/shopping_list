"""Module contains class ShoppingListTable"""
from typing import Union

from PyQt5.QtGui import QColor  # pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QTableWidgetItem

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_list.shopping_list import ShoppingList
from lib.shopping_list.shopping_list_item import ShoppingListItem
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.tables.base_table_widget import BaseTableWidget

UNORDERED_COLOR = QColor(255, 150, 150)


class ShoppingListTable(BaseTableWidget):
    """Implementation of shopping list table"""
    def __init__(self, items_list: Union[ShoppingList, ShoppingArticlesList], columns_count: int, *args, **kwargs):
        super().__init__(items_list, columns_count, *args, **kwargs)
        self.setObjectName(ObjectNames.SHOPPING_LIST_TABLE)
        LIST_SIGNALS.shop_changed.connect(self._shop_changed)
        LIST_SIGNALS.category_list_changed.connect(self._category_list_changed)

    @staticmethod
    def _get_item_by_column(item: ShoppingListItem, column: int):
        return [item.article.name, item.article.category, item.amount][column]

    def _color_unordered_rows(self):
        for i in range(self.rowCount()):
            if self.item(i, 0).text() in [x.article.name for x in self.items_list.unordered_items]:
                for j in range(3):
                    self.item(i, j).setBackground(UNORDERED_COLOR)

    def _shop_changed(self):
        self.items_list.sort_by_shop()
        LIST_SIGNALS.list_changed.emit()

    def _items_modifier(self):
        self.items_list.sort_by_shop()
        return self.items_list

    def _amount_changed(self, article: ShoppingArticle, new_value: str) -> bool:
        article.amount = new_value
        return True

    def _category_change(self, list_item: ShoppingListItem, new_value: str) -> bool:
        self.items_list.shopping_articles_list.edit_category(list_item.article, new_value)
        self.items_list.sort_by_shop()
        return True

    def _action_if_existing_article(self, list_item: ShoppingListItem, shopping_list: ShoppingList,
                                    new_value: str) -> bool:
        try:
            new_article = shopping_list.shopping_articles_list.get_article_by_name(new_value)
            new_list_item = ShoppingListItem(new_article, list_item.amount, list_item.checked)
            shopping_list.remove(list_item)
            shopping_list.append(new_list_item)
            return True
        except AttributeError:
            return False

    def _action_if_non_existing_article(self, list_item: ShoppingListItem, shopping_list: ShoppingList,
                                        new_value: str) -> bool:
        shopping_list.add_new_article(new_value, list_item.article.category, list_item.amount, list_item.checked)
        shopping_list.remove(list_item)
        list_item.article.selection -= 1
        return True

    def _category_list_changed(self):
        self.items_list.sort_by_shop()
        LIST_SIGNALS.list_changed.emit()

    def populate_table(self):
        """
        Populate items with table, if needed modify items and color cells
        """
        self.blockSignals(True)
        modified_list = self._items_modifier()
        self.setRowCount(len(modified_list))
        for row, item in enumerate(modified_list):
            for column, value in zip(range(self._columns_count), [item.article.name, item.article.category, item.amount]):
                self.setItem(row, column, QTableWidgetItem(str(value)))
        self._color_unordered_rows()
        self.blockSignals(False)
