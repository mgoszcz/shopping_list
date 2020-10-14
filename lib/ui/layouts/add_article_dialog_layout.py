from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QDialogButtonBox

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.widgets.category_combo_box import CategoryComboBox


class AddArticleDialogLayout(QVBoxLayout):

    def __init__(self, items_list: ShoppingArticlesList):
        super(AddArticleDialogLayout, self).__init__()
        self._items_list = items_list
        self.product = QLineEdit()
        self.category = CategoryComboBox(self._items_list.shopping_categories)
        self.ok_button = QPushButton('OK')
        self.cancel_button = QPushButton('Cancel')
        product_layout = QHBoxLayout()
        product_layout.addWidget(QLabel('Produkt: '))
        product_layout.addWidget(self.product)
        category_layout = QHBoxLayout()
        category_layout.addWidget(QLabel('Kategoria: '))
        category_layout.addWidget(self.category)
        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonbox = QDialogButtonBox(btn)
        self.addLayout(product_layout)
        self.addLayout(category_layout)
        self.addWidget(self.buttonbox)
