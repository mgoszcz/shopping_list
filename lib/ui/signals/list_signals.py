from PyQt5.QtCore import QObject, pyqtSignal


class ListSignals(QObject):
    list_changed = pyqtSignal()
    category_list_changed = pyqtSignal()
    shop_changed = pyqtSignal()
    shop_list_changed = pyqtSignal()

    def emit_all(self):
        self.list_changed.emit()
        self.category_list_changed.emit()
        self.shop_changed.emit()
        self.shop_list_changed.emit()


LIST_SIGNALS = ListSignals()
