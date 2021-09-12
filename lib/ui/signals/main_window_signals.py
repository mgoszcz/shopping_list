from PyQt5.QtCore import QObject, pyqtSignal


class MainWindowSignals(QObject):
    window_moved = pyqtSignal()


MAIN_WINDOW_SIGNALS = MainWindowSignals()
