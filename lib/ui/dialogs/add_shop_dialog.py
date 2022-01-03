"""
class AddShopDialog
"""
import os
from shutil import copyfile
from typing import Union

from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.file_manager.file_object import FileObject, FileObjectException
from lib.shop.shop import Shop
from lib.shop.shops_list import ShopsList
from lib.ui.dialogs.error_dialog import ErrorDialog
from lib.ui.icons.icons import ShoppingListIcon
from lib.ui.layouts.add_shop_dialog_layout import AddShopDialogLayout
from lib.ui.object_names.object_names import ObjectNames
from resources.paths.paths import SHOPS_ICONS_PATH


class AddEditShopDialog(QDialog):
    """
    Implementation of add shop dialog
    """

    def __init__(self, shops_list: ShopsList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_SHOP_DIALOG)
        self._shops_list = shops_list
        self.setWindowIcon(ShoppingListIcon.q_icon())
        self.new_shop = AddShopDialogLayout()
        self.setLayout(self.new_shop)
        self._shop_name = None

        self.new_shop.buttonbox.rejected.connect(self.reject)
        self.new_shop.buttonbox.accepted.connect(self.accept_button)

    def _validate_fields(self, ignore_name: bool = False) -> bool:
        if not ignore_name:
            shop_name = self.new_shop.name.text()
            if not shop_name:
                ErrorDialog('Shop name cannot be empty').exec_()
                return False
            try:
                self._shops_list.get_shop_by_name(shop_name)
                ErrorDialog('Shop name already exists').exec_()
                return False
            except AttributeError:
                pass
        logo_path = self.new_shop.logo.file_path.text()
        if not logo_path:
            return True
        filename, file_extension = os.path.splitext(logo_path)
        if not os.path.exists(logo_path):
            ErrorDialog('Logo file path does not exist.').exec_()
            return False
        if file_extension.lower() not in ('.png', '.jpg', '.bmp'):
            ErrorDialog('Invalid extension on logo file. Allowed extensions: bmp, png, jpg.').exec_()
            return False
        return True

    def _set_shop_logo(self, logo_path: str) -> Union[str, bool]:
        if not logo_path:
            return ''
        filename, file_extension = os.path.splitext(logo_path)
        if not os.path.isdir(SHOPS_ICONS_PATH):
            os.mkdir(SHOPS_ICONS_PATH)
        new_icon_file = FileObject(os.path.join(SHOPS_ICONS_PATH, f'{self._shop_name}{file_extension.lower()}'))
        if new_icon_file.exists():
            try:
                new_icon_file.remove()
            except FileObjectException as e:
                ErrorDialog(str(e)).exec_()
                return False
        copyfile(logo_path, new_icon_file.file_path)
        return new_icon_file.file_path

    def accept_button(self):
        """
        Action on pressing OK button
        """


class AddShopDialog(AddEditShopDialog):

    def __init__(self, shops_list: ShopsList, *args, **kwargs):
        super().__init__(shops_list, *args, **kwargs)
        self.setWindowTitle('Dodaj sklep...')

    def accept_button(self):
        """
        Action on pressing OK button - add shop to list
        """
        if not self._validate_fields():
            return
        self._shop_name = self.new_shop.name.text()
        logo_path = self.new_shop.logo.file_path.text()
        new_logo_path = self._set_shop_logo(logo_path)
        if new_logo_path is not False:
            self._shops_list.add_shop(self._shop_name, new_logo_path)
            self.accept()


class EditShopDialog(AddEditShopDialog):
    def __init__(self, shops_list: ShopsList, current_shop: Shop, *args, **kwargs):
        super().__init__(shops_list, *args, **kwargs)
        self._current_shop = current_shop
        self.setWindowTitle(f'Edytuj sklep {self._current_shop.name}...')
        self.new_shop.name.setText(self._current_shop.name)
        self.new_shop.logo.file_path.setText(self._current_shop.logo)

    def _remove_old_logo_file_if_needed(self, old_logo: str, name_changed: bool) -> None:
        if old_logo:
            if not self.new_shop.logo.file_path.text() or name_changed:
                if FileObject(old_logo).exists():
                    try:
                        FileObject(old_logo).remove()
                    except FileObjectException as e:
                        print(e)

    def accept_button(self):
        """
        Action on pressing OK button - add shop to list
        """
        old_name = self._current_shop.name
        name_changed = False
        if not self._validate_fields(old_name == self.new_shop.name.text()):
            return
        old_logo = self._current_shop.logo
        self._shop_name = self.new_shop.name.text()
        if old_name != self._shop_name:
            self._current_shop.name = self.new_shop.name.text()
            name_changed = True
        if old_logo != self.new_shop.logo.file_path.text():
            new_logo_path = self._set_shop_logo(self.new_shop.logo.file_path.text())
            if new_logo_path is not False:
                self._current_shop.logo = new_logo_path
            else:
                ErrorDialog('Logo was unchanged').exec_()
            self._remove_old_logo_file_if_needed(old_logo, name_changed)
        self.accept()
