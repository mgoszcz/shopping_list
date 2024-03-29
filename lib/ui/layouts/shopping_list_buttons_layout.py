"""
Module contains classes _ShoppingListButtons, _PrinterButtons and ShoppingListButtonsLayout
"""
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout  # pylint: disable=no-name-in-module

from lib.printer.printer_interface import PrinterInterface
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.widgets.buttons.article_list_button import ArticleListButton
from lib.ui.widgets.buttons.clear_list_button import ClearListButton
from lib.ui.widgets.buttons.print_button import PrintButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.combo_boxes.printer_combo_box import PrinterComboBox


class _ShoppingListButtons(QHBoxLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_button = RemoveButton()
        self.clear_list_button = ClearListButton()
        self.article_list_button = ArticleListButton()
        self.addWidget(self.remove_button)
        self.addWidget(self.clear_list_button)
        self.addWidget(self.article_list_button)


class _PrinterButtons(QHBoxLayout):

    def __init__(self, printer: PrinterInterface, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.printer_selector = PrinterComboBox(printer)
        self.print_button = PrintButton()
        self.addWidget(self.printer_selector)
        self.addWidget(self.print_button)
        if not printer.supported:
            self.print_button.setDisabled(True)
            self.printer_selector.setDisabled(True)


class ShoppingListButtonsLayout(QVBoxLayout):
    """
    Layout with buttons handling shopping list and printing
    """
    def __init__(self, printer: PrinterInterface, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.SHOPPING_LIST_BUTTONS_LAYOUT)
        self.shopping_list_buttons = _ShoppingListButtons()
        self.printer_buttons = _PrinterButtons(printer)
        self.addLayout(self.shopping_list_buttons)
        self.addLayout(self.printer_buttons)
