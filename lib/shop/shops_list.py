from lib.lists.list_without_duplicates import ShoppingListWithoutDuplicates
from lib.shop.shop import Shop


class ShopsList(ShoppingListWithoutDuplicates):

    def add_shop(self, name: str, logo: str = None):
        self.append(Shop(name, logo))

    def get_shop_by_name(self, name: str) -> Shop:
        for shop in self:
            if shop.name == name:
                return shop
        raise AttributeError(f'Shop {name} not found')

    def remove_shop(self, name: str):
        self.remove(self.get_shop_by_name(name))
