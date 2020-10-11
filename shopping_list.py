import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtRemoveInputHook, QTimer

from lib.shopping_list_interface import ShoppingListInterface
from lib.ui.main_window import MainWindow

interface = ShoppingListInterface()

app = QApplication(sys.argv)
window = MainWindow(interface)
window.show()

timer = QTimer()
timer.timeout.connect(lambda: None)
timer.start(100)

app.exec_()
pass