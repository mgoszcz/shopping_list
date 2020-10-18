from typing import Union

from lib.lists.list_without_duplicates import ShoppingListWithoutDuplicates
from lib.save_load.events import SAVE_NEEDED
from lib.shop.shop import Shop
from lib.ui.signals.list_signals import LIST_SIGNALS


class ShopsList(ShoppingListWithoutDuplicates):

    def __init__(self):
        super(ShopsList, self).__init__()
        self._selected_shop = None

    @property
    def selected_shop(self) -> Union[Shop, None]:
        return self._selected_shop

    @selected_shop.setter
    def selected_shop(self, value):
        if value not in self:
            raise AttributeError(f'Shop {value} does not exist')
        self._selected_shop = value
        SAVE_NEEDED.set()
        LIST_SIGNALS.shop_changed.emit()

    def clear_selected_shop(self):
        self._selected_shop = None
        LIST_SIGNALS.shop_changed.emit()

    def add_shop(self, name: str, logo: str = None):
        shop = Shop(name, logo)
        self.append(shop)
        self.selected_shop = shop

    def get_shop_by_name(self, name: str) -> Shop:
        for shop in self:
            if shop.name == name:
                return shop
        raise AttributeError(f'Shop {name} not found')

    def remove_shop(self, name: str):
        shop = self.get_shop_by_name(name)
        self.remove(shop)
        if self.selected_shop == shop:
            self.clear_selected_shop()
