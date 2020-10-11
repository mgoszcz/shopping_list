from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from lib.shopping_list_interface import ShoppingListInterface
from lib.ui.layouts.add_article_layout import AddArticleLayout
from lib.ui.layouts.shop_layout import ShopLayout
from lib.ui.layouts.shopping_list_layout import ShoppingListLayout
from lib.ui.widgets.combo_box import ArticleComboBox


class MainWindow(QMainWindow):

    def __init__(self, interface: ShoppingListInterface,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interface = interface
        self.layout = QVBoxLayout()
        self._add_article_layout = AddArticleLayout(self.interface.shopping_list)
        self._shopping_list_layout = ShoppingListLayout(self.interface.shopping_list)
        self._shop_layout = ShopLayout()

        self.layout.addLayout(self._add_article_layout)
        self.layout.addLayout(self._shopping_list_layout)
        self.layout.addLayout(self._shop_layout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
