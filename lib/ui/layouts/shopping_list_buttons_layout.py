from PyQt5.QtWidgets import QHBoxLayout  # pylint: disable=no-name-in-module

from lib.ui.widgets.buttons.article_list_button import ArticleListButton
from lib.ui.widgets.buttons.clear_list_button import ClearListButton
from lib.ui.widgets.buttons.edit_button import EditButton
from lib.ui.widgets.buttons.print_button import PrintButton
from lib.ui.widgets.buttons.remove_button import RemoveButton


class ShoppingListButtonsLayout(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.print_button = PrintButton()
        self.remove_button = RemoveButton()
        self.clear_list_button = ClearListButton()
        self.article_list_button = ArticleListButton()
        self.addWidget(self.print_button)
        self.addWidget(self.remove_button)
        self.addWidget(self.clear_list_button)
        self.addWidget(self.article_list_button)
