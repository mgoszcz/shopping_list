"""
Module contains CategoriesDialog
"""
from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.shop.shops_list import ShopsList
from lib.ui.layouts.categories_dialog_layout import CategoriesDialogLayout


class CategoriesDialog(QDialog):
    """
    Implementation of categories dialog used by shops
    """
    def __init__(self, shop_list: ShopsList):
        super().__init__()
        self._shops_list = shop_list
        self.layout = CategoriesDialogLayout(self._shops_list)
        self.setLayout(self.layout)
