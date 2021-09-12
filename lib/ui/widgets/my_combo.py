from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QPoint
from PyQt5.QtWidgets import QLineEdit, QDialog, QListWidget, QHBoxLayout

from lib.search.article_search import ArticleSearch


"""
Filtrowanie wrzucic w list widget
poprawcowac nad focusem - po kliknieciu w text edit focus powinien pozostac w text edit
dopracowac resize
pomyslec nad rozmiarem
pomyslec nad sorrtowaniem w dropdown
obsluzyc selekcje
ogarnac 'Dodaj...' - powiniene zawsze sei wsywietlac na gorze
"""


class FocusSignal(QObject):
    text_edit_focus_in = pyqtSignal()
    text_edit_focus_out = pyqtSignal()
    list_view_focus_in = pyqtSignal()
    list_view_focus_out = pyqtSignal()

FOCUS_SIGNAL = FocusSignal()

class TextEdit(QLineEdit):
    def focusInEvent(self, QFocusEvent):
        super().focusInEvent(QFocusEvent)
        print('in')
        FOCUS_SIGNAL.text_edit_focus_in.emit()

    def focusOutEvent(self, QFocusEvent):
        super().focusOutEvent(QFocusEvent)
        print('out')
        FOCUS_SIGNAL.text_edit_focus_out.emit()

class MyListWidget(QListWidget):

    def __init__(self, items_list):
        super().__init__()
        self.items_list = items_list
        self.displayed_items = items_list

        self.populate_list()

    def populate_list(self):
        self.clear()
        for item in self.displayed_items:
            self.addItem(item.name)

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        print('listwidget out')
        FOCUS_SIGNAL.list_view_focus_out.emit()

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        print('listwidget in')
        FOCUS_SIGNAL.list_view_focus_in.emit()

class MyDropDown(QDialog):

    def __init__(self, parent, items_list):
        super().__init__(parent=parent, flags=Qt.FramelessWindowHint)
        self.list_widget = MyListWidget(items_list)
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        print(self.parent())
        print(self.parent().x(), self.parent().y(), self.parent().width(), self.parent().height())
        geometry = self.parent().mapToGlobal(QPoint(0, self.parent().y()))
        # globa = self.test_entry.mapToGlobal(QPoint(0, y))

        # self.setModal(False)
        # self.setWindowModality(Qt.NonModal)

        self.setGeometry(geometry.x(), geometry.y(), self.parent().width(), 100)


class MyCombo(QHBoxLayout):

    def __init__(self, items_list):
        super().__init__()
        self.test_entry = TextEdit()
        self.dropdown = MyDropDown(parent=self.test_entry, items_list=items_list)
        # self.widget = QDialog(parent=self.test_entry, flags=Qt.FramelessWindowHint)

        self.addWidget(self.test_entry)

        FOCUS_SIGNAL.text_edit_focus_in.connect(self.new_widget)
        FOCUS_SIGNAL.text_edit_focus_out.connect(self.close_widget)
        FOCUS_SIGNAL.list_view_focus_out.connect(self.close_widget)
        self.test_entry.textChanged.connect(self.filter_article)

    def close_widget(self):
        if self.dropdown.list_widget.hasFocus():
            return
        if self.test_entry.hasFocus():
            return
        print('dd')
        self.dropdown.close()

    def new_widget(self):

        if self.dropdown.isVisible():
            return
        y = self.test_entry.height()
        geometry = self.dropdown.parent().mapToGlobal(QPoint(0, y))
        self.dropdown.setGeometry(geometry.x(), geometry.y(), self.dropdown.parent().width(), 200)
        self.dropdown.show()
        # self.widget.setFocus()

    def filter_article(self):
        current_text = self.test_entry.text()
        if not current_text:
            self.dropdown.list_widget.displayed_items = self.dropdown.list_widget.items_list
        else:
            print('a')
            self.dropdown.list_widget.displayed_items = ArticleSearch(self.dropdown.list_widget.items_list).search_by_name(current_text)
        self.dropdown.list_widget.populate_list()