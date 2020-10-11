from PyQt5.QtWidgets import QVBoxLayout

from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.layouts.shopping_list_buttons_layout import ShoppingListButtonsLayout
from lib.ui.widgets.shopping_list import ShoppingListTable


class ShoppingListLayout(QVBoxLayout):

    def __init__(self, shopping_list: ShoppingList):
        super().__init__()
        self._shopping_list = shopping_list
        self._shopping_list_table = ShoppingListTable(self._shopping_list)
        self._shopping_list_buttons_layout = ShoppingListButtonsLayout()
        self.addWidget(self._shopping_list_table)
        self.addLayout(self._shopping_list_buttons_layout)