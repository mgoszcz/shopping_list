from typing import List

from lib.printer.printer_interface import PrinterInterface


class PrinterMac(PrinterInterface):
    """
    Class handling printing
    """
    def print(self):
        """
        Print current shopping list
        """

    @property
    def printers(self) -> List[str]:
        """
        Get system printers
        :return: list of printers names
        """
        return []

    @property
    def printer_name(self):
        return 'No printers on MacOs'
