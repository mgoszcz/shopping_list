"""
class AddShopDialog
"""
from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.shop.shops_list import ShopsList
from lib.ui.icons.icons import ShoppingListIcon
from lib.ui.layouts.add_shop_dialog_layout import AddShopDialogLayout


class AddShopDialog(QDialog):
    """
    Implementation of add shop dialog
    """
    def __init__(self, shops_list: ShopsList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._shops_list = shops_list
        self.setWindowTitle('Dodaj sklep...')
        self.setWindowIcon(ShoppingListIcon.q_icon())
        self.new_shop = AddShopDialogLayout()
        self.setLayout(self.new_shop)

        self.new_shop.buttonbox.rejected.connect(self.reject)
        self.new_shop.buttonbox.accepted.connect(self.accept_button)

    def accept_button(self):
        """
        Action on pressing OK button - add shop to list
        """
        shop_name = self.new_shop.name.text()
        self._shops_list.add_shop(shop_name)
        self.accept()
