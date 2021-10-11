"""Module contains AddArticleComboBox class"""
from typing import Optional

from PyQt5.QtCore import Qt  # pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QHBoxLayout  # pylint: disable=no-name-in-module

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.add_article_combo_signals import ADD_ARTICLE_COMBO_SIGNALS
from lib.ui.widgets.combo_boxes.add_article_combo_box._add_article_dropdown import AddArticleDropdown
from lib.ui.widgets.combo_boxes.add_article_combo_box._add_article_text_entry import AddArticleTextEntry


class AddArticleComboBox(QHBoxLayout):
    """This layout keeps all widgets needed to implement combo box"""
    def __init__(self, items_list: ShoppingArticlesList, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_ARTICLE_COMBOBOX)
        self.text_entry = AddArticleTextEntry()
        self._items = items_list
        self.dropdown = AddArticleDropdown(parent=self.text_entry, items_list=items_list)

        self.addWidget(self.text_entry)

        ADD_ARTICLE_COMBO_SIGNALS.text_edit_focus_in.connect(self.show_dropdown)
        ADD_ARTICLE_COMBO_SIGNALS.text_edit_focus_out.connect(self.close_dropdown)
        ADD_ARTICLE_COMBO_SIGNALS.list_view_focus_out.connect(self.close_dropdown)
        ADD_ARTICLE_COMBO_SIGNALS.text_edit_key_down.connect(self.set_focus_on_dropdown)
        ADD_ARTICLE_COMBO_SIGNALS.list_view_key_pressed.connect(self.type_on_key_press)
        self.text_entry.textChanged.connect(self.filter_article)
        self.dropdown.list_widget.itemClicked.connect(self.select_article_from_dropdown)
        ADD_ARTICLE_COMBO_SIGNALS.list_view_return_pressed.connect(self.select_article_from_dropdown)

    def type_on_key_press(self, key: int) -> None:
        """Type letter in test entry when letter key is pressed in list widget"""
        self.text_entry.activateWindow()
        if key not in (Qt.Key_Backspace, Qt.Key_Alt):
            self.text_entry.insert(chr(key).lower())

    def close_dropdown(self) -> None:
        """Close dropdown when focus is NOT in text entry OR list widget"""
        if self.dropdown.list_widget.hasFocus():
            return
        if self.text_entry.hasFocus():
            return
        self.dropdown.close()

    def show_dropdown(self) -> None:
        """Show dropdown when text edit activated"""
        if self.dropdown.isVisible():
            return
        self.dropdown.set_dropdown_geometry()
        self.dropdown.show()
        self.text_entry.activateWindow()

    def filter_article(self) -> None:
        """Filter articles displayed in dropdown when text in text entry changes"""
        self.dropdown.list_widget.filter_article(self.text_entry.text())

    def select_article_from_dropdown(self) -> None:
        """action on selection of item in dropdown"""
        article_name = self.dropdown.list_widget.currentItem().text()
        if article_name and article_name != 'Dodaj...':
            self.text_entry.setText(article_name)
        elif article_name == 'Dodaj...':
            dialog = AddNewArticleDialog(self._items)
            dialog.exec_()

    def set_focus_on_dropdown(self) -> None:
        """Set focus on dropdown when Down button pressed in text entry"""
        self.dropdown.list_widget.setCurrentRow(0)
        self.dropdown.activateWindow()

    def get_current_article(self) -> Optional[ShoppingArticle]:
        """
        Get article object for selected article name
        """
        if self.text_entry.text() == 'Dodaj...':
            raise RuntimeError('Text entry text is "Dodaj..."')
        try:
            return self._items.get_article_by_name(self.text_entry.text())
        except AttributeError:
            return None
