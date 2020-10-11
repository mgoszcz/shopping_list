from PyQt5.QtWidgets import QHBoxLayout, QLabel

from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.buttons.category_list_button import CategoryListButton
from lib.ui.widgets.buttons.remove_button import RemoveButton


class ShopLayout(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.addWidget(QLabel('SKLEP:'))
        self.addWidget(QLabel('<nazwa>'))
        self.addWidget(QLabel('<logo>'))
        self.addWidget(AddButton())
        self.addWidget(RemoveButton())
        self.addWidget(CategoryListButton())
