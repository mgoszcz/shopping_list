from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QPoint
from PyQt5.QtWidgets import QLineEdit, QDialog, QListWidget, QHBoxLayout

from lib.search.article_search import ArticleSearch
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.main_window_signals import MAIN_WINDOW_SIGNALS

"""
POC ready, let's implement it!
"""

DROPDOWN_KEYS_CHANGE_FOCUS = (Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9,
                              Qt.Key_0, Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F, Qt.Key_G, Qt.Key_H,
                              Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L, Qt.Key_M, Qt.Key_N, Qt.Key_O, Qt.Key_P, Qt.Key_Q,
                              Qt.Key_R, Qt.Key_S, Qt.Key_T, Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X, Qt.Key_Y, Qt.Key_Z,
                              Qt.Key_Space, Qt.Key_Backspace, Qt.Key_Alt)


class FocusSignal(QObject):
    text_edit_focus_in = pyqtSignal()
    text_edit_focus_out = pyqtSignal()
    list_view_focus_in = pyqtSignal()
    list_view_focus_out = pyqtSignal()
    list_view_key_pressed = pyqtSignal(int)
    list_view_return_pressed = pyqtSignal()
    text_edit_key_down = pyqtSignal()


FOCUS_SIGNAL = FocusSignal()


class TextEdit(QLineEdit):

    def __init__(self):
        super().__init__()

        FOCUS_SIGNAL.list_view_key_pressed.connect(self.setFocus)

    def focusInEvent(self, QFocusEvent):
        """POTRZEBNE"""
        super().focusInEvent(QFocusEvent)
        print('in')
        FOCUS_SIGNAL.text_edit_focus_in.emit()

    def focusOutEvent(self, QFocusEvent):
        """POTRZEBNE"""
        super().focusOutEvent(QFocusEvent)
        print('out')
        FOCUS_SIGNAL.text_edit_focus_out.emit()

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        """POTRZEBNE"""
        super().keyReleaseEvent(a0)
        if a0.key() == Qt.Key_Down:
            FOCUS_SIGNAL.text_edit_key_down.emit()
        # print(a0.key() == Qt.Key_Down)


class MyListWidget(QListWidget):

    def __init__(self, items_list):
        super().__init__()
        self._items_list = items_list
        self.displayed_items = [item.name for item in items_list]

        self._populate_list()

    def _populate_list(self):
        """POTRZEBNE"""
        self.clear()
        self.addItem('Dodaj...')
        for item in sorted(self.displayed_items):
            self.addItem(item)

    def filter_article(self, current_text):
        """POTRZEBNE"""
        if not current_text:
            self.displayed_items = [item.name for item in self._items_list]
        else:
            print('a')
            self.displayed_items = [item.name for item in ArticleSearch(self._items_list).search_by_name(current_text)]
        self._populate_list()

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        """POTRZEBNE"""
        print('listwidget out')
        FOCUS_SIGNAL.list_view_focus_out.emit()

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        """POTRZEBNE"""
        print('listwidget in')
        FOCUS_SIGNAL.list_view_focus_in.emit()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        """
        POTRZEBNE
        musi dzialac
        Escape, Home, End, Up, Down, pageup, pagedown,
        musi dzialac altgr + key
        """
        print('klawisz: ' + str(a0.key()))
        # print(a0.nativeModifiers())
        if a0.key() in (Qt.Key_Return, Qt.Key_Enter):
            print('obsluz enter')
            FOCUS_SIGNAL.list_view_return_pressed.emit()
        elif a0.key() in DROPDOWN_KEYS_CHANGE_FOCUS:
            print('guzik')
            FOCUS_SIGNAL.list_view_key_pressed.emit(a0.key())
        elif a0.key() == Qt.Key_AltGr:
            print('altgr')
        else:
            super().keyPressEvent(a0)
        print('-----')


class MyDropDown(QDialog):
    """WSZYSTKO POTRZEBNE"""
    def __init__(self, parent, items_list):
        super().__init__(parent=parent, flags=Qt.FramelessWindowHint)
        self.list_widget = MyListWidget(items_list)
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        MAIN_WINDOW_SIGNALS.window_moved.connect(self.set_position_and_geometry)

    def set_position_and_geometry(self):
        geometry = self.parent().mapToGlobal(QPoint(0, self.parent().height()))
        parent = self.parentWidget()
        while not parent.objectName() == ObjectNames.MAIN_WINDOW:
            parent = parent.parentWidget()
        main_window_height = parent.height()
        self.setGeometry(geometry.x(), geometry.y(), self.parent().width(), int(main_window_height / 2))


class MyCombo(QHBoxLayout):

    def __init__(self, items_list):
        super().__init__()
        self.test_entry = TextEdit()
        self._items = items_list
        self.dropdown = MyDropDown(parent=self.test_entry, items_list=items_list)
        # self.dropdown.setFocusProxy(self.test_entry)
        # self.widget = QDialog(parent=self.test_entry, flags=Qt.FramelessWindowHint)

        self.addWidget(self.test_entry)

        FOCUS_SIGNAL.text_edit_focus_in.connect(self.new_widget)
        FOCUS_SIGNAL.text_edit_focus_out.connect(self.close_widget)
        FOCUS_SIGNAL.list_view_focus_out.connect(self.close_widget)
        FOCUS_SIGNAL.text_edit_key_down.connect(self.set_focus_on_dropdown)
        FOCUS_SIGNAL.list_view_key_pressed.connect(self.aaa)
        self.test_entry.textChanged.connect(self.filter_article)
        self.dropdown.list_widget.itemClicked.connect(self.select_article_from_dropdown)
        FOCUS_SIGNAL.list_view_return_pressed.connect(self.select_article_from_dropdown)

    def aaa(self, key):
        """POTRZEBNE"""
        print(f'aaa {key}')
        self.test_entry.activateWindow()
        if key not in (Qt.Key_Backspace, Qt.Key_Alt):
            self.test_entry.insert(chr(key).lower())

    def close_widget(self):
        """POTRZEBNE"""
        if self.dropdown.list_widget.hasFocus():
            return
        if self.test_entry.hasFocus():
            return
        print('dd')
        self.dropdown.close()

    def new_widget(self):
        """POTRZEBNE"""
        if self.dropdown.isVisible():
            return
        self.dropdown.set_position_and_geometry()
        self.dropdown.show()
        self.test_entry.activateWindow()

    def filter_article(self):
        """POTRZEBNE"""
        self.dropdown.list_widget.filter_article(self.test_entry.text())
        print('jestem')

    def select_article_from_dropdown(self):
        """POTRZEBNE"""
        article_name = self.dropdown.list_widget.currentItem().text()
        if article_name and article_name != 'Dodaj...':
            self.test_entry.setText(article_name)
        elif article_name == 'Dodaj...':
            dialog = AddNewArticleDialog(self._items)
            dialog.exec_()

    def set_focus_on_dropdown(self):
        """POTRZEBNE"""
        self.dropdown.list_widget.setCurrentRow(0)
        self.dropdown.activateWindow()

    def filter_article(self):
        """POTRZEBNE"""
        self.dropdown.list_widget.filter_article(self.test_entry.text())
        print('jestem')
