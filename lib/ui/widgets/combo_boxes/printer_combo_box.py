"""
Module contains class PrinterComboBox
"""
from PyQt5.QtWidgets import QComboBox  # pylint: disable=no-name-in-module

from lib.printer.printer_interface import PrinterInterface
from lib.ui.object_names.object_names import ObjectNames


class PrinterComboBox(QComboBox):
    """
    Class with printer combobox implementation
    """
    def __init__(self, printer: PrinterInterface, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.PRINTER_COMBO_BOX)
        self._printer = printer

        if not self._printer.supported:
            self.addItems(['Printers are not supported on this OS'])
            self.setCurrentText('Printers are not supported on this OS')
            return

        self._populate_list()
        self.setEditable(False)
        self.setCurrentText(self._printer.printer_name)

        self.currentTextChanged.connect(self._set_printer)

    def _populate_list(self) -> None:
        """Fill combobox with printers"""
        selected_item = self.currentText()
        for i in reversed(range(0, self.count())):
            self.removeItem(i)
        self.addItems(self._printer.printers)
        if selected_item and selected_item in self._printer.printers:
            self.setCurrentText(selected_item)

    def _set_printer(self) -> None:
        """set current printer"""
        self._printer.printer_name = self.currentText()

    def showPopup(self) -> None:  # pylint: disable=invalid-name
        """
        Overload showPopup method to invoke list refresh when opening popup
        """
        self._populate_list()
        super().showPopup()
