import os


from lib.shopping_article_list.shopping_list import ShoppingList


class Printer:
    def __init__(self, shopping_list: ShoppingList):
        if os.name == 'posix':
            from lib.printer.printer_mac import PrinterMac
            self.printer = PrinterMac()
        else:
            from lib.printer.printer_win import PrinterWin
            self.printer = PrinterWin(shopping_list)
        print(self)
        print(self.printer)
