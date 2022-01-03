"""Module contains class ShopsList"""
from typing import Union

from lib.file_manager.file_object import FileObject, FileObjectException
from lib.lists.list_without_duplicates import ShoppingListWithoutDuplicates
from lib.save_load.events import SAVE_NEEDED
from lib.shop.shop import Shop
from lib.shopping_categories.category_list import CategoryList
from lib.ui.signals.list_signals import LIST_SIGNALS


class ShopsList(ShoppingListWithoutDuplicates):
    """Shops list implementation"""
    def __init__(self, categories: CategoryList):
        super().__init__()
        self._selected_shop = None
        self.categories = categories

    @property
    def selected_shop(self) -> Union[Shop, None]:
        """Get currently selected shop"""
        return self._selected_shop

    @selected_shop.setter
    def selected_shop(self, value):
        """Set currently selected shop (save and refresh GUI)"""
        if value:
            if value not in self:
                raise AttributeError(f'Shop {value} does not exist')
        self._selected_shop = value
        SAVE_NEEDED.set()
        LIST_SIGNALS.shop_changed.emit()

    def clear_selected_shop(self):
        """Clear selected shop value (on remove)"""
        self._selected_shop = None
        LIST_SIGNALS.shop_changed.emit()

    def add_shop(self, name: str, logo: str = None):
        """
        Add new shop
        :param name: name of shop
        :param logo: shop's logo
        """
        shop = Shop(name, logo)
        self.append(shop)
        self.selected_shop = shop
        LIST_SIGNALS.shop_list_changed.emit()

    def get_shop_by_name(self, name: str) -> Shop:
        """
        Get shop with specific name from list
        :param name: name of shop
        """
        for shop in self:
            if shop.name == name:
                return shop
        raise AttributeError(f'Shop {name} not found')

    def remove_shop(self, name: str):
        """
        Remove shop with specific name from list
        :param name: name of shop
        """
        shop = self.get_shop_by_name(name)
        logo = shop.logo
        self.remove(shop)
        if logo:
            try:
                FileObject(logo).remove()
            except FileObjectException as e:
                print(str(e))
        if self.selected_shop == shop:
            if self:
                self.selected_shop = self[0]
            else:
                self.clear_selected_shop()
        LIST_SIGNALS.shop_list_changed.emit()
