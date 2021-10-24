"""
class AddShopDialog
"""
import os
from shutil import copyfile

from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.shop.shops_list import ShopsList
from lib.ui.dialogs.error_dialog import ErrorDialog
from lib.ui.icons.icons import ShoppingListIcon
from lib.ui.layouts.add_shop_dialog_layout import AddShopDialogLayout
from lib.ui.object_names.object_names import ObjectNames


class AddShopDialog(QDialog):
    """
    Implementation of add shop dialog
    """

    def __init__(self, shops_list: ShopsList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_SHOP_DIALOG)
        self._shops_list = shops_list
        self.setWindowTitle('Dodaj sklep...')
        self.setWindowIcon(ShoppingListIcon.q_icon())
        self.new_shop = AddShopDialogLayout()
        self.setLayout(self.new_shop)
        self._shop_name = None

        self.new_shop.buttonbox.rejected.connect(self.reject)
        self.new_shop.buttonbox.accepted.connect(self.accept_button)

    def _set_shop_logo(self, logo_path: str):
        if not logo_path:
            return ''
        filename, file_extension = os.path.splitext(logo_path)
        if not os.path.exists(logo_path):
            ErrorDialog('Logo file path does not exist.')
            return
        if file_extension not in ('.png', '.jpg', '.bmp'):
            ErrorDialog('Invalid extension on logo file. Allowed extensions: bmp, png, jpg.')
            return
        if not os.path.isdir('resources/icons/shops'):
            os.mkdir('resources/icons/shops')
        new_icon_path = f'resources/icons/shops/{self._shop_name}{file_extension}'
        copyfile(logo_path, new_icon_path)
        return new_icon_path

    def accept_button(self):
        """
        Action on pressing OK button - add shop to list
        """
        self._shop_name = self.new_shop.name.text()
        logo_path = self.new_shop.logo.file_path.text()
        new_logo_path = self._set_shop_logo(logo_path)
        self._shops_list.add_shop(self._shop_name, new_logo_path)
        self.accept()
