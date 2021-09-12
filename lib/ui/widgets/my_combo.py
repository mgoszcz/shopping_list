from PyQt5.QtCore import QObject, pyqtSignal, Qt, QPoint
from PyQt5.QtWidgets import QLineEdit, QDialog, QListWidget, QHBoxLayout


class FocusSignal(QObject):
    focus_in = pyqtSignal()
    focus_out = pyqtSignal()

FOCUS_SIGNAL = FocusSignal()

class TextEdit(QLineEdit):
    def focusInEvent(self, QFocusEvent):
        super().focusInEvent(QFocusEvent)
        print('in')
        FOCUS_SIGNAL.focus_in.emit()

    def focusOutEvent(self, QFocusEvent):
        super().focusOutEvent(QFocusEvent)
        print('out')
        FOCUS_SIGNAL.focus_out.emit()

class Dialog(QDialog):
    def focusOutEvent(self, *args, **kwargs):
        print('b')
        FOCUS_SIGNAL.focus_out.emit()
        print('a')

    def focusInEvent(self, *args, **kwargs):
        print('c')

    def closeEvent(self, QCloseEvent):
        print('d')
        if self.parent().hasFocus():
            QCloseEvent.ignore()
            print('foc')
        else:
            super().closeEvent(QCloseEvent)
        print('d')

class MyCombo(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.test_entry = TextEdit()
        self.widget = Dialog(parent=self.test_entry, flags=Qt.FramelessWindowHint)

        self.addWidget(self.test_entry)

        FOCUS_SIGNAL.focus_in.connect(self.new_widget)

    def new_widget(self):

        if self.widget.isVisible():
            return
        list = QListWidget()
        lyt = QHBoxLayout()
        lyt.addWidget(list)
        self.widget.setLayout(lyt)
        y = self.test_entry.height()
        globa = self.test_entry.mapToGlobal(QPoint(0, y))
        print(globa, globa.x(), globa.y())
        self.widget.setModal(False)
        print(self.widget.isModal())
        self.widget.setWindowModality(Qt.NonModal)
        self.widget.setGeometry(globa.x(), globa.y(), self.test_entry.width(), 100)
        # widget.width = 10
        # widget.height = 10
        # widget.x = x
        # widget.y = y
        self.widget.show()
        self.widget.setFocus()
