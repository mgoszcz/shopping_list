"""Module contains class MainWindowSignals"""
from PyQt5.QtCore import QObject, pyqtSignal  # pylint: disable=no-name-in-module


class MainWindowSignals(QObject):
    """Signals emitted by main window"""
    window_moved = pyqtSignal()


MAIN_WINDOW_SIGNALS = MainWindowSignals()
