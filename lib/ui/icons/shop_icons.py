"""Module with class ShopIcon"""
from PyQt5.QtGui import QPixmap

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


DEFAULT_SHOP_ICON = ShopIcon('C:\\Users\\mgoszcz\\repo\\shopping_list\\resources\\icons\\default_shop.png')
