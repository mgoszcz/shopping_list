"""
Module contains class ShoppingListLayout
"""
from PyQt5.QtCore import Qt  # pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QVBoxLayout  # pylint: disable=no-name-in-module

from lib.printer.printer import Printer
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.dialogs.articles_dialog import ArticlesDialog
from lib.ui.layouts.shopping_list_buttons_layout import ShoppingListButtonsLayout
from lib.ui.widgets.tables.shopping_list_table import ShoppingListTable


class ShoppingListLayout(QVBoxLayout):
    """
    Class setting layout for shopping list field
    """
    def __init__(self, shopping_list: ShoppingList):
        super().__init__()
        self._shopping_list = shopping_list
        self._printer = Printer(self._shopping_list)
        self._shopping_list_table = ShoppingListTable(self._shopping_list, 3)
        self._shopping_list_buttons_layout = ShoppingListButtonsLayout(self._printer)
        self.addWidget(self._shopping_list_table)
        self.addLayout(self._shopping_list_buttons_layout)

        self._shopping_list_buttons_layout.shopping_list_buttons.remove_button.pressed.connect(self.remove_article)
        self._shopping_list_buttons_layout.shopping_list_buttons.clear_list_button.pressed.connect(self.clear_list)
        self._shopping_list_buttons_layout.shopping_list_buttons.article_list_button.pressed.connect(
            self.open_articles_list)
        self._shopping_list_buttons_layout.printer_buttons.print_button.pressed.connect(self.print_list)

    def remove_article(self):
        """
        Action after pressing remove button
        """
        self._shopping_list_table.blockSignals(True)
        article = self._shopping_list_table.item(self._shopping_list_table.currentRow(), 0).text()
        self._shopping_list.remove_article(article)
        self._shopping_list_table.blockSignals(False)

    def clear_list(self):
        """
        Action after pressing clear list button
        """
        self._shopping_list.clear()

    def open_articles_list(self):
        """
        Action after pressing articles list button (opens articles list dialog)
        """
        self._shopping_list_table.blockSignals(True)
        dialog = ArticlesDialog(self._shopping_list)
        dialog.exec_()
        self._shopping_list_table.blockSignals(False)

    def select_item(self, item_name: str):
        """
        Select specific article on list, used when adding new article to select newly added article
        :param item_name: name of article
        """
        items = self._shopping_list_table.findItems(item_name, Qt.MatchExactly)
        if len(items) > 1:
            columns = [item.column() for item in items]
            if columns.count(0) > 1:
                raise RuntimeError('More than one item found')
        if items:
            row = self._shopping_list_table.row(items[0])
            self._shopping_list_table.setCurrentCell(row, 2)
            self._shopping_list_table.scrollToItem(items[0])

    def print_list(self):
        """
        Print shopping list
        """
        self._printer.print()
