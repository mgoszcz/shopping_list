"""
Module contains MainWindow class
"""
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget  # pylint: disable=no-name-in-module

from lib.shopping_list_interface import ShoppingListInterface
from lib.ui.layouts.add_article_layout import AddArticleLayout
from lib.ui.layouts.backup_layout import BackupLayout
from lib.ui.layouts.shop_layout import ShopLayout
from lib.ui.layouts.shopping_list_layout import ShoppingListLayout


class MainWindow(QMainWindow):
    """
    Implementation of main window
    """
    def __init__(self, interface: ShoppingListInterface, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interface = interface
        self.layout = QVBoxLayout()
        self._add_article_layout = AddArticleLayout(self.interface.shopping_list)
        self._shopping_list_layout = ShoppingListLayout(self.interface.shopping_list)
        self._shop_layout = ShopLayout(self.interface.shops)
        self._backup_layout = BackupLayout(self.interface.backup_manager)

        self.layout.addLayout(self._add_article_layout)
        self.layout.addLayout(self._shopping_list_layout)
        self.layout.addLayout(self._shop_layout)
        self.layout.addLayout(self._backup_layout)

        self._add_article_layout.add_button.pressed.connect(self.add_article_to_shopping_list)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def add_article_to_shopping_list(self):
        """
        Method using two different widgets to add article to shopping list
        """
        article = self._add_article_layout.add_article_to_list()
        self._shopping_list_layout.select_item(article.name)
