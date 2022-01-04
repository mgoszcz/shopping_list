"""Module with class ShopIcon"""
from PyQt5.QtGui import QPixmap

from resources.paths.paths import DEFAULT_SHOP_ICON_PATH

SHOP_ICON_SIZE = 25


class ShopIcon:
    """Class used to return qpixmap object for specific path"""

    def __init__(self, path: str) -> None:
        self.path = path

    def get_pixmap(self) -> QPixmap:
        """Get qPixmap Object with proper size"""
        pixmap = QPixmap(self.path)
        pixmap = pixmap.scaled(SHOP_ICON_SIZE, SHOP_ICON_SIZE)
        return pixmap


DEFAULT_SHOP_ICON = ShopIcon(DEFAULT_SHOP_ICON_PATH)
