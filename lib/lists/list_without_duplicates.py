"""
Module contains classes StringListWithoutDuplicates, ShopAndArticleListWithoutDuplicates
"""
from typing import Union, TYPE_CHECKING

from lib.save_load.events import SAVE_NEEDED
from lib.ui.signals.list_signals import LIST_SIGNALS

if TYPE_CHECKING:
    from lib.shop.shop import Shop
    from lib.shopping_article.shopping_article import ShoppingArticle
    from lib.shopping_list.shopping_list_item import ShoppingListItem


class StringListWithoutDuplicates(list):
    """
    Implementation of list of strings without duplicates allowed
    """

    def __init__(self):
        super().__init__()
        self.custom_sort = False

    def append(self, element: str) -> None:
        """
        Append item to list only if such item does not exist on list and trigger save and list changed signal
        If list is not sorted by user then sort alphabetically
        :param element: string to be added to list
        """
        if not element.lower() in self:
            super().append(element.lower())
            if not self.custom_sort:
                self.sort()
            SAVE_NEEDED.set()
            LIST_SIGNALS.category_list_changed.emit()

    def remove(self, item) -> None:
        """
        Remove item from list and trigger auto save and list changed signal
        :param item: item to be removed
        """
        super().remove(item)
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()


class ShopAndArticleListWithoutDuplicates(list):
    """
    Implementation of shopping list that does not allow duplicates
    """

    def append(self, element: Union['ShoppingListItem', 'ShoppingArticle', 'Shop']) -> None:
        """
        Append item to list and trigged auto save and list changed signal
        :param element: element to be added (ShoppingArticle or Shop)
        """
        self.append_silent(element)
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()

    def append_silent(self, element: Union['ShoppingArticle', 'Shop']) -> None:
        """
        Append item to list without save and list changed signal.
        Raise an error when element already on the list
        :param element: element to be added (ShoppingArticle or Shop)
        """
        if not element.name.lower() in [item.name.lower() for item in self]:
            super().append(element)
        else:
            raise AttributeError(f'Item with name {element.name} already exists')

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()

    def remove_silent(self, item) -> None:
        """
        Remove item from list without auto save and list changed signal triggering
        :param item: item to be removed
        """
        super().remove(item)

    def remove(self, item) -> None:
        """
        Remove item from list and trigger auto save and list changed signal
        :param item: item to be removed
        """
        self.remove_silent(item)
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()

    def clear_silent(self):
        """
        Clear whole list without auto save and list changed signal triggering
        """
        super().clear()

    def clear(self):
        """
        Clear list and trigger auto save and list changed signal
        """
        self.clear_silent()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()


class ShoppingListWithoutDuplicates(ShopAndArticleListWithoutDuplicates):
    """Implementation of shopping list without duplicates (used in shopping list view)"""

    def append_silent(self, element: Union['ShoppingListItem']) -> None:
        """
        Append item to list without save and list changed signal.
        Raise an error when element already on the list
        :param element: element to be added (ShoppingListItem)
        """
        if not element.article.name.lower() in [item.article.name.lower() for item in self]:
            super(ShopAndArticleListWithoutDuplicates, self).append(element)
        else:
            raise AttributeError(f'Item with name {element.article.name} already exists')
