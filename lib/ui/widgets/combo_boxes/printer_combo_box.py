"""
Module contains class PrinterComboBox
"""
from PyQt5.QtWidgets import QComboBox  # pylint: disable=no-name-in-module

from lib.printer.printer import Printer
from lib.ui.object_names.object_names import ObjectNames


class PrinterComboBox(QComboBox):
    """
    Class with printer combobox implementation
    """
    def __init__(self, printer: Printer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.PRINTER_COMBO_BOX)
        self._printer = printer

        self._populate_list()
        self.setEditable(False)
        self.setCurrentText(self._printer.printer_name)

        self.currentTextChanged.connect(self._set_printer)

    def _populate_list(self):
        for i in reversed(range(0, self.count())):
            self.removeItem(i)
        self.addItems(self._printer.printers)

    def _set_printer(self):
        self._printer.printer_name = self.currentText()

    def showPopup(self) -> None:  # pylint: disable=invalid-name
        """
        Overload showPopup method to invoke list refresh when opening popup
        """
        self._populate_list()
        super().showPopup()
