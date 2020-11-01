import win32gui
import win32print
import win32ui
from win32con import DMPAPER_A5, DMORIENT_PORTRAIT

from lib.shopping_article_list.shopping_list import ShoppingList


class Printer:
    def __init__(self, shopping_list: ShoppingList):
        self._shopping_list = shopping_list
        self.printer_name = win32print.GetDefaultPrinter()
        self.dpi = 300
        self.format = DMPAPER_A5
        self.orientation = DMORIENT_PORTRAIT
        self.items_per_column = 46
        self.file_path = None
        self.margin = 100
        self._devmode = None
        self._text_format = '{} {}'
        print(self.printer_name)

    def _printer_initialize(self):
        hprinter = win32print.OpenPrinter(self.printer_name)
        self._devmode = win32print.GetPrinter(hprinter, 2)["pDevMode"]
        self._devmode.PaperSize = self.format
        self._devmode.PrintQuality = self.dpi
        self._devmode.Orientation = self.orientation

    def _get_max_text_size(self, document):
        max_length = 0
        max_height = 0
        for item in self._shopping_list:
            size = document.GetTextExtent(f'{item.name} {item.amount}')
            if size[0] > max_length:
                max_length = size[0]
            if size[1] > max_height:
                max_height = size[1]
        return max_length + 100, max_height

    def _prepare_document(self):
        hdc = win32gui.CreateDC("WINSPOOL", self.printer_name, self._devmode)
        document = win32ui.CreateDCFromHandle(hdc)
        length, height = self._get_max_text_size(document)
        if self.file_path:
            document.StartDoc('ShoppingList', self.file_path)
        else:
            document.StartDoc('ShoppingList')
        document.StartPage()
        i = 1
        x = self.margin
        for value in self._shopping_list:
            if i == self.items_per_column + 1:
                x += length
                i = 1
            document.TextOut(x, i * height, f'{value.name} {value.amount}')
            i += 1
        document.EndPage()
        document.EndDoc()

    def print(self):
        if not self._shopping_list:
            raise RuntimeError('Shopping List is empty')
        self._printer_initialize()
        self._prepare_document()
