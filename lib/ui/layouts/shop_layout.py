from PyQt5.QtWidgets import QHBoxLayout, QLabel

from lib.shop.shops_list import ShopsList
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.buttons.category_list_button import CategoryListButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.combo_boxes.shops_combo_box import ShopsComboBox


class ShopLayout(QHBoxLayout):

    def __init__(self, shops_list: ShopsList):
        super().__init__()
        self._shops_list = shops_list
        self._shops_combo_box = ShopsComboBox(self._shops_list)
        self.addWidget(QLabel('SKLEP:'))
        self.addWidget(self._shops_combo_box)
        self.addWidget(QLabel('<logo>'))
        self.addWidget(AddButton())
        self.addWidget(RemoveButton())
        self.addWidget(CategoryListButton())

        self._shops_combo_box.activated.connect(self._shop_changed)

    def _shop_changed(self):
        if self._shops_list.selected_shop.name != self._shops_combo_box.currentText():
            self._shops_list.selected_shop = self._shops_list.get_shop_by_name(self._shops_combo_box.currentText())