"""
Module contains PrinterStatics class
"""
from win32con import DMPAPER_A5, DMORIENT_PORTRAIT


class PrinterStatics:
    """
    Static values used by Printer class
    """
    FORMAT = DMPAPER_A5
    ORIENTATION = DMORIENT_PORTRAIT
    DPI = 300
    ITEMS_PER_COLUMN = 46
    MARGIN = 100
