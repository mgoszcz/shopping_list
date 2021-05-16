"""
Module contains class PrinterComboBox
"""
from PyQt5.QtWidgets import QComboBox

from lib.printer.printer import Printer


class PrinterComboBox(QComboBox):
    """
    Class with printer combobox implementation
    """
    def __init__(self, printer: Printer):
        super().__init__()
        self._printer = printer

        self._populate_list()
        self.setEditable(False)
        self.setCurrentText(self._printer.printer_name)

        # self.highlighted.connect(self._populate_list)
        self.currentTextChanged.connect(self._set_printer)

    def _populate_list(self):
        for i in reversed(range(0, self.count())):
            self.removeItem(i)
        self.addItems(self._printer.printers)
        print(self._printer.printers)
        # self.setCurrentText(self._printer.printer_name)

    def _set_printer(self):
        self._printer.printer_name = self.currentText()

    def showPopup(self) -> None:
        """
        Overload showPopup method to invoke list refresh when opening popup
        """
        self._populate_list()
        super().showPopup()
