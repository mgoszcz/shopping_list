from PyQt5.QtCore import QObject, pyqtSignal


class ListSignals(QObject):
    list_changed = pyqtSignal()
    category_list_changed = pyqtSignal()
    shop_changed = pyqtSignal()
    shop_list_changed = pyqtSignal()


LIST_SIGNALS = ListSignals()
