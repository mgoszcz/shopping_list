from PyQt5.QtWidgets import QHBoxLayout

from lib.ui.widgets.buttons.article_list_button import ArticleListButton
from lib.ui.widgets.buttons.clear_list_button import ClearListButton
from lib.ui.widgets.buttons.edit_button import EditButton
from lib.ui.widgets.buttons.print_button import PrintButton
from lib.ui.widgets.buttons.remove_button import RemoveButton


class ShoppingListButtonsLayout(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.addWidget(PrintButton())
        self.addWidget(RemoveButton())
        self.addWidget(EditButton())
        self.addWidget(ClearListButton())
        self.addWidget(ArticleListButton())
