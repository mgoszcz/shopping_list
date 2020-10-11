from PyQt5.QtCore import QObject, pyqtSignal


class ListSignals(QObject):
    list_changed = pyqtSignal()


LIST_SIGNALS = ListSignals()
