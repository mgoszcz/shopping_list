"""Module contains _AddArticleListWidget and AddArticleDropdown classes"""
from PyQt5 import QtGui  # pylint: disable=no-name-in-module
from PyQt5.QtCore import Qt, QPoint  # pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QListWidget, QDialog, QHBoxLayout  # pylint: disable=no-name-in-module

from lib.search.article_search import ArticleSearch
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.getters.get_parent_object import get_parent_object
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.add_article_combo_signals import ADD_ARTICLE_COMBO_SIGNALS
from lib.ui.signals.main_window_signals import MAIN_WINDOW_SIGNALS

DROPDOWN_KEYS_CHANGE_FOCUS = (Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9,
                              Qt.Key_0, Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F, Qt.Key_G, Qt.Key_H,
                              Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L, Qt.Key_M, Qt.Key_N, Qt.Key_O, Qt.Key_P, Qt.Key_Q,
                              Qt.Key_R, Qt.Key_S, Qt.Key_T, Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X, Qt.Key_Y, Qt.Key_Z,
                              Qt.Key_Space, Qt.Key_Backspace, Qt.Key_Alt)


class _AddArticleListWidget(QListWidget):
    """List of articles disaplyed in add article combo box"""

    def __init__(self, items_list: ShoppingArticlesList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_ARTICLE_LIST_WIDGET)
        self._items_list = items_list
        self.displayed_items = [item.name for item in items_list]

        self._populate_list()

    def _populate_list(self):
        """Populate list of articles"""
        self.clear()
        self.addItem('Dodaj...')
        for item in sorted(self.displayed_items):
            self.addItem(item)

    def filter_article(self, current_text):
        """Filter articles list, they are filtered based on text entry string"""
        if not current_text:
            self.displayed_items = [item.name for item in self._items_list]
        else:
            self.displayed_items = [item.name for item in ArticleSearch(self._items_list).search_by_name(current_text)]
        self._populate_list()

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:  # pylint: disable=invalid-name, unused-argument, no-self-use
        """Overload method to have specific signal emitted"""
        ADD_ARTICLE_COMBO_SIGNALS.list_view_focus_out.emit()

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:  # pylint: disable=invalid-name, unused-argument, no-self-use
        """Overload method to have specific signal emitted"""
        ADD_ARTICLE_COMBO_SIGNALS.list_view_focus_in.emit()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:  # pylint: disable=invalid-name
        """Overload method to have specific signal emitted"""
        if a0.key() in (Qt.Key_Return, Qt.Key_Enter):
            ADD_ARTICLE_COMBO_SIGNALS.list_view_return_pressed.emit()
        elif a0.key() in DROPDOWN_KEYS_CHANGE_FOCUS:
            ADD_ARTICLE_COMBO_SIGNALS.list_view_key_pressed.emit(a0.key())
        else:
            super().keyPressEvent(a0)


class AddArticleDropdown(QDialog):
    """add article dropdown implementation"""
    def __init__(self, parent, items_list) -> None:
        super().__init__(parent=parent, flags=Qt.FramelessWindowHint)
        self.setObjectName(ObjectNames.ADD_ARTICLE_DROPDOWN)
        self.list_widget = _AddArticleListWidget(items_list)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        MAIN_WINDOW_SIGNALS.window_moved.connect(self.set_dropdown_geometry)

    def set_dropdown_geometry(self) -> None:
        """Set position and size of dropdown"""
        geometry = self.parent().mapToGlobal(QPoint(0, self.parent().height()))
        main_window = get_parent_object(self, ObjectNames.MAIN_WINDOW)
        main_window_height = main_window.height()
        self.setGeometry(geometry.x(), geometry.y(), self.parent().width(), int(main_window_height / 2))
