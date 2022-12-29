"""
Module contains MainWindow class
"""
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget  # pylint: disable=no-name-in-module

from lib.shopping_list_interface import ShoppingListInterface
from lib.ui.layouts.add_article_layout import AddArticleLayout
from lib.ui.layouts.backup_layout import BackupLayout
from lib.ui.layouts.shop_layout import ShopLayout
from lib.ui.layouts.shopping_list_layout import ShoppingListLayout
from lib.ui.signals.add_article_combo_signals import ADD_ARTICLE_COMBO_SIGNALS
from lib.ui.signals.main_window_signals import MAIN_WINDOW_SIGNALS
from lib.ui.icons.icons import ShoppingListIcon
from lib.ui.object_names.object_names import ObjectNames


class MainWindow(QMainWindow):
    """
    Implementation of main window
    """
    def __init__(self, interface: ShoppingListInterface, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.MAIN_WINDOW)
        self.setWindowTitle('Shopping List')
        self.setWindowIcon(ShoppingListIcon.q_icon())
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
        ADD_ARTICLE_COMBO_SIGNALS.text_edit_return_key.connect(self.add_article_to_shopping_list)

        widget = QWidget()
        widget.setObjectName(ObjectNames.MAIN_WINDOW_CENTRAL_WIDGET)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def moveEvent(self, a0: QtGui.QMoveEvent) -> None:  # pylint: disable=invalid-name, unused-argument, no-self-use
        MAIN_WINDOW_SIGNALS.window_moved.emit()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:  # pylint: disable=invalid-name, unused-argument, no-self-use
        MAIN_WINDOW_SIGNALS.window_moved.emit()

    def add_article_to_shopping_list(self):
        """
        Method using two different widgets to add article to shopping list
        """
        article = self._add_article_layout.add_article_to_list()
        if article:
            self._shopping_list_layout.shopping_list_table.activateWindow()
            self._shopping_list_layout.select_item(article.name)
