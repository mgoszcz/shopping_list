"""Implementation of ShopsComboBox class"""
from PyQt5.QtWidgets import QComboBox  # pylint: disable=no-name-in-module

from lib.shop.shops_list import ShopsList
from lib.ui.signals.list_signals import LIST_SIGNALS


class ShopsComboBox(QComboBox):
    """Implementation of combobox to select current shop"""
    def __init__(self, shops_list: ShopsList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = shops_list

        self._populate_list()
        self.setEditable(False)

        LIST_SIGNALS.shop_list_changed.connect(self._populate_list)

    def select_current_shop(self):
        """Select currently selected shop on initialization or when removing shop"""
        if self.items.selected_shop:
            self.setCurrentIndex(self.items.index(self.items.selected_shop))
        else:
            self.setCurrentText('')

    def _populate_list(self):
        for i in reversed(range(0, self.count())):
            self.removeItem(i)
        self.addItems([x.name for x in self.items])
        self.select_current_shop()
