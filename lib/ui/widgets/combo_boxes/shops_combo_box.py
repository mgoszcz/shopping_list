from PyQt5.QtWidgets import QComboBox

from lib.shop.shops_list import ShopsList


class ShopsComboBox(QComboBox):

    def __init__(self, shops_list: ShopsList):
        super().__init__()
        self.items = shops_list

        self._populate_list()
        self.setEditable(False)

    def _populate_list(self):
        for i in reversed(range(1, self.count())):
            self.removeItem(i)
        self.addItems([x.name for x in self.items])
        self.setCurrentIndex(self.items.index(self.items.selected_shop))
