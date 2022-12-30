"""Module contains Printer class"""
import os

from lib.shopping_list.shopping_list import ShoppingList


class Printer:
    """Factory class that determines type of printer based on current OS"""

    def __init__(self, shopping_list: ShoppingList):
        if os.name == 'posix':
            from lib.printer.printer_mac import PrinterMac  # pylint: disable=import-outside-toplevel
            self.printer = PrinterMac()
        else:
            from lib.printer.printer_win import PrinterWin  # pylint: disable=import-outside-toplevel
            self.printer = PrinterWin(shopping_list)
