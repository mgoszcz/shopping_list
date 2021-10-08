"""Module contains ShopLayout class"""
from PyQt5.QtWidgets import QHBoxLayout, QLabel  # pylint: disable=no-name-in-module

from lib.shop.shops_list import ShopsList
from lib.ui.dialogs.add_shop_dialog import AddShopDialog
from lib.ui.dialogs.categories_dialog import CategoriesDialog
from lib.ui.dialogs.confirm_dialog import ConfirmDialog
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.buttons.category_list_button import CategoryListButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.combo_boxes.shops_combo_box import ShopsComboBox


class ShopLayout(QHBoxLayout):
    """Implementation of shop field layout"""
    def __init__(self, shops_list: ShopsList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName('shop_layout')
        self._shops_list = shops_list
        self._shops_combo_box = ShopsComboBox(self._shops_list)
        self._add_shop_button = AddButton(self.parentWidget())
        self._remove_shop_button = RemoveButton()
        self._category_list_button = CategoryListButton()
        self.addWidget(QLabel('SKLEP:'))
        self.addWidget(self._shops_combo_box)
        self.addWidget(QLabel('<logo>'))
        self.addWidget(self._add_shop_button)
        self.addWidget(self._remove_shop_button)
        self.addWidget(self._category_list_button)
        self._disable_buttons()

        self._shops_combo_box.activated.connect(self._shop_changed)
        self._add_shop_button.pressed.connect(self._add_shop)
        self._remove_shop_button.pressed.connect(self._remove_shop)
        self._category_list_button.pressed.connect(self._categories_dialog)

    def _shop_changed(self):
        self._disable_buttons()
        if self._shops_list.selected_shop:
            if self._shops_list.selected_shop.name == self._shops_combo_box.currentText():
                return
        self._shops_list.selected_shop = self._shops_list.get_shop_by_name(self._shops_combo_box.currentText())

    def _add_shop(self):
        dialog = AddShopDialog(self._shops_list)
        dialog.exec_()
        self._disable_buttons()

    def _remove_shop(self):
        shop_name = self._shops_combo_box.currentText()
        if shop_name:
            dialog = ConfirmDialog(f'Czy jesteś pewien aby usunąć sklep {shop_name}?')
            if dialog.exec_():
                self._shops_list.remove_shop(shop_name)
        self._disable_buttons()

    def _categories_dialog(self):
        dialog = CategoriesDialog(self._shops_list)
        dialog.exec_()

    def _disable_buttons(self):
        self._remove_shop_button.setDisabled(False)
        self._category_list_button.setDisabled(False)
        shop_name = self._shops_combo_box.currentText()
        if not shop_name:
            self._remove_shop_button.setDisabled(True)
            self._category_list_button.setDisabled(True)
