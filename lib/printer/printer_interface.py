from abc import ABC, abstractmethod
from typing import List


class PrinterInterface(ABC):

    @property
    @abstractmethod
    def printer_name(self) -> str:
        """Return current printer name"""

    @printer_name.setter
    @abstractmethod
    def printer_name(self, value: str) -> None:
        """Sets current printer name"""

    @abstractmethod
    def print(self) -> None:
        """
        Print current shopping list
        """


    @property
    @abstractmethod
    def printers(self) -> List[str]:
        """
        Get system printers
        :return: list of printers names
        """
