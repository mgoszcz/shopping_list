"""
Module contains Printer class
"""
from typing import List, Tuple

import win32gui
import win32print
import win32ui

from lib.printer.printer_interface import PrinterInterface
from lib.printer.printer_statics import PrinterStatics
from lib.shopping_list.shopping_list import NewShoppingList


class PrinterWin(PrinterInterface):
    """
    Class handling printing
    """
    def __init__(self, shopping_list: NewShoppingList):
        self._shopping_list = shopping_list
        self._printer_name = win32print.GetDefaultPrinter()
        self._printers = None
        self.file_path = None
        self._devmode = None
        self._supported = True
        print(self._printer_name)

    def _printer_initialize(self):
        hprinter = win32print.OpenPrinter(self._printer_name)
        self._devmode = win32print.GetPrinter(hprinter, 2)["pDevMode"]
        self._devmode.PaperSize = PrinterStatics.FORMAT
        self._devmode.PrintQuality = PrinterStatics.DPI
        self._devmode.Orientation = PrinterStatics.ORIENTATION

    def _get_max_text_size(self, document) -> Tuple[int, int]:
        max_length = 0
        max_height = 0
        for item in self._shopping_list:
            size = document.GetTextExtent(f'{item.article.name} {item.amount}')
            if size[0] > max_length:
                max_length = size[0]
            if size[1] > max_height:
                max_height = size[1]
        return max_length + 100, max_height

    def _prepare_document(self):
        hdc = win32gui.CreateDC("WINSPOOL", self._printer_name, self._devmode)
        document = win32ui.CreateDCFromHandle(hdc)
        length, height = self._get_max_text_size(document)
        if self.file_path:
            document.StartDoc('ShoppingList', self.file_path)
        else:
            document.StartDoc('ShoppingList')
        document.StartPage()
        i = 1
        x_pos = PrinterStatics.MARGIN
        for value in self._shopping_list:
            if i == PrinterStatics.ITEMS_PER_COLUMN + 1:
                x_pos += length
                i = 1
            document.TextOut(x_pos, i * height, f'{value.article.name} {value.amount}')
            i += 1
        document.EndPage()
        document.EndDoc()


    @property
    def supported(self) -> bool:
        return self._supported

    @property
    def printer_name(self) -> str:
        return self._printer_name

    @printer_name.setter
    def printer_name(self, value) -> None:
        self._printer_name = value

    def print(self):
        """
        Print current shopping list
        """
        if not self._shopping_list:
            raise RuntimeError('Shopping List is empty')
        self._printer_initialize()
        self._prepare_document()

    @property
    def printers(self) -> List[str]:
        """
        Get system printers
        :return: list of printers names
        """
        self._printers = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)]
        return self._printers
