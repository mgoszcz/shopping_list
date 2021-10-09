"""
Contains AddArticleDialogLayout class
"""

from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QLabel, QPushButton, \
    QGridLayout  # pylint: disable=no-name-in-module

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.widgets.combo_boxes.category_combo_box import CategoryComboBox


class AddArticleDialogLayout(QGridLayout):
    """
    Add new article dialog
    """

    def __init__(self, items_list: ShoppingArticlesList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_ARTICLE_DIALOG_LAYOUT)
        self._items_list = items_list
        self.product = QLineEdit()
        self.category = CategoryComboBox(self._items_list.shopping_categories)
        self.addWidget(QLabel('Produkt: '), 0, 0)
        self.addWidget(self.product, 0, 1)
        self.addWidget(QLabel('Kategoria: '), 1, 0)
        self.addWidget(self.category, 1, 1)
        self.button_layout = QHBoxLayout()
        self.ok_button = QPushButton('Ok')
        self.cancel = QPushButton('Cancel')
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel)
        self.addLayout(self.button_layout, 2, 1)
        self.error = QLabel('')
        self.addWidget(self.error, 3, 0, 1, 2)
