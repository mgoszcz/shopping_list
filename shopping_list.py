"""
Main module to start shopping list application

For debugging purposes there is timer added to have a possibility to pause application and interact with console
"""

# TODO:
"""
Testy
    1. Zapis i odczyt obrazu w bazie na serwerze
    2. Zapis sciezki do obrazu w sklepie
    3. Dodawanie, usuwanie sklepu z logiem i bez
        kopiowanie pliku pod nazwe sklepu
        usuwanie pliku przy usuwaniu sklepu
        brak dostepu do pliku, zanlokowany plik
            Dodac obsluge PermissionError
    4. Edycja sklepu
        z logiem na bez loga - usuwanie pliku i wyswietlanie w gui
        z logiem na z logiem - zmiana obrazu pod nazwa sklepu (plus brak dostepu)
        bez loga na z logiem - obraz jest kopiowany pod nazwa sklepu
        zmiana nazwy + z logiem na bez loga - usuwanie pliku i wyswietlanie w gui
        zmiana nazwy + z logiem na z logiem - kopiowanie nowego loga pod nowa nazwe, usuniecie starego loga pod stara nazwa 
        bez loga na z logiem - obraz jest kopiowany pod nową nazwa sklepu
        
    
"""

import sys


from PyQt5.QtWidgets import QApplication  # pylint: disable=no-name-in-module
from PyQt5.QtCore import QTimer  # pylint: disable=no-name-in-module

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
