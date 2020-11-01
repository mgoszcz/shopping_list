from PyQt5.QtWidgets import QVBoxLayout

from lib.printer.printer import Printer
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.dialogs.articles_dialog import ArticlesDialog
from lib.ui.layouts.shopping_list_buttons_layout import ShoppingListButtonsLayout
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.tables.shopping_list_table import ShoppingListTable


class ShoppingListLayout(QVBoxLayout):

    def __init__(self, shopping_list: ShoppingList):
        super().__init__()
        self._shopping_list = shopping_list
        self._shopping_list_table = ShoppingListTable(self._shopping_list, 3)
        self._shopping_list_buttons_layout = ShoppingListButtonsLayout()
        self.addWidget(self._shopping_list_table)
        self.addLayout(self._shopping_list_buttons_layout)

        self._shopping_list_buttons_layout.remove_button.pressed.connect(self.remove_article)
        self._shopping_list_buttons_layout.clear_list_button.pressed.connect(self.clear_list)
        self._shopping_list_buttons_layout.article_list_button.pressed.connect(self.open_articles_list)
        self._shopping_list_buttons_layout.print_button.pressed.connect(self.print_list)

    def remove_article(self):
        self._shopping_list_table.blockSignals(True)
        article = self._shopping_list_table.item(self._shopping_list_table.currentRow(), 0).text()
        self._shopping_list.remove_article(article)
        self._shopping_list_table.blockSignals(False)

    def clear_list(self):
        self._shopping_list.clear()

    def open_articles_list(self):
        self._shopping_list_table.blockSignals(True)
        dialog = ArticlesDialog(self._shopping_list)
        dialog.exec_()
        self._shopping_list_table.blockSignals(False)

    def print_list(self):
        printer = Printer(self._shopping_list)
        # printer.file_path = 'c:\\Users\\marci\\Documents\\abc.pdf'
        # printer.printer_name = 'Microsoft Print to PDF'
        printer.print()
