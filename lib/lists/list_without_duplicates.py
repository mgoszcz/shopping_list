from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from lib.shop.shop import Shop
    from lib.shopping_article.shopping_article import ShoppingArticle


class StringListWithoutDuplicates(list):

    def append(self, element: str) -> None:
        if not element.lower() in self:
            super().append(element.lower())


class ShoppingListWithoutDuplicates(list):

    def append(self, element: Union['ShoppingArticle', 'Shop']) -> None:
        if not element.name.lower() in self:
            super().append(element)
        else:
            raise AttributeError(f'Item with name {element.name} already exists')
