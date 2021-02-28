"""
Module contains ListSignals class
"""
from PyQt5.QtCore import QObject, pyqtSignal  # pylint: disable=no-name-in-module


class ListSignals(QObject):
    """
    Implementation of Qt signals for changes handling
    """
    list_changed = pyqtSignal()
    category_list_changed = pyqtSignal()
    shop_changed = pyqtSignal()
    shop_list_changed = pyqtSignal()

    def emit_all(self):
        """
        Emit all signals from class
        """
        self.list_changed.emit()
        self.category_list_changed.emit()
        self.shop_changed.emit()
        self.shop_list_changed.emit()


LIST_SIGNALS = ListSignals()
