from PyQt5.QtWidgets import QDialog

from lib.shop.shops_list import ShopsList
from lib.ui.layouts.add_shop_dialog_layout import AddShopDialogLayout


class AddShopDialog(QDialog):
    def __init__(self, shops_list: ShopsList):
        super().__init__()
        self._shops_list = shops_list
        self.new_shop = AddShopDialogLayout()
        self.setLayout(self.new_shop)

        self.new_shop.buttonbox.rejected.connect(self.reject)
        self.new_shop.buttonbox.accepted.connect(self.accept_button)

    def accept_button(self):
        shop_name = self.new_shop.name.text()
        self._shops_list.add_shop(shop_name)
        self.accept()
