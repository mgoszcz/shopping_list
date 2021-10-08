"""
Module contains CategoriesDialog
"""
from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.shop.shops_list import ShopsList
from lib.ui.icons.icons import ShoppingListIcon
from lib.ui.layouts.categories_dialog_layout import CategoriesDialogLayout
from lib.ui.object_names.object_names import ObjectNames


class CategoriesDialog(QDialog):
    """
    Implementation of categories dialog used by shops
    """
    def __init__(self, shop_list: ShopsList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CATEGORIES_DIALOG)
        self._shops_list = shop_list
        self.setWindowTitle('Kategorie artykułów w sklepie')
        self.setWindowIcon(ShoppingListIcon.q_icon())
        self.layout = CategoriesDialogLayout(self._shops_list)
        self.setLayout(self.layout)
