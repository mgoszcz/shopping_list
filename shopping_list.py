"""
Main module to start shopping list application

For debugging purposes there is timer added to have a possibility to pause application and interact with console
"""


import sys


from PyQt5.QtWidgets import QApplication  # pylint: disable=no-name-in-module
from PyQt5.QtCore import QTimer  # pylint: disable=no-name-in-module

from lib.file_manager.file_object import FileObjectException
from lib.shopping_list_interface import ShoppingListInterface
from lib.ui.dialogs.error_dialog import ErrorDialog
from lib.ui.main_window import MainWindow

app = QApplication(sys.argv)
try:
    interface = ShoppingListInterface()
except FileObjectException as e:
    ErrorDialog(str(e)).exec_()
    sys.exit(2)
window = MainWindow(interface)
window.show()

timer = QTimer()
timer.timeout.connect(lambda: None)
timer.start(100)

app.exec_()
