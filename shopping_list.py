"""
Main module to start shopping list application

For debugging purposes there is timer added to have a possibility to pause application and interact with console
"""


import sys


from PyQt5.QtWidgets import QApplication  # pylint: disable=no-name-in-module
from PyQt5.QtCore import QTimer  # pylint: disable=no-name-in-module

from lib.shopping_list_interface import ShoppingListInterface
from lib.ui.main_window import MainWindow

interface = ShoppingListInterface()
interface.shops.get_shop_by_name('Auchan').logo = 'resources/icons/download.png'

app = QApplication(sys.argv)
window = MainWindow(interface)
window.show()

timer = QTimer()
timer.timeout.connect(lambda: None)
timer.start(100)

app.exec_()
