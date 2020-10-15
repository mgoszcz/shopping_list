from typing import Union, TYPE_CHECKING

from lib.save_load.events import SAVE_NEEDED
from lib.ui.signals.list_signals import LIST_SIGNALS

if TYPE_CHECKING:
    from lib.shop.shop import Shop
    from lib.shopping_article.shopping_article import ShoppingArticle


class StringListWithoutDuplicates(list):

    def append(self, element: str) -> None:
        if not element.lower() in self:
            super().append(element.lower())
            SAVE_NEEDED.set()
            LIST_SIGNALS.category_list_changed.emit()

    def __setitem__(self, key, value):
        super(StringListWithoutDuplicates, self).__setitem__(key, value)
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()

    def remove(self, item) -> None:
        super(StringListWithoutDuplicates, self).remove(item)
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()


class ShoppingListWithoutDuplicates(list):

    def append(self, element: Union['ShoppingArticle', 'Shop']) -> None:
        if not element.name.lower() in [item.name.lower() for item in self]:
            super().append(element)
            SAVE_NEEDED.set()
            LIST_SIGNALS.list_changed.emit()
        else:
            raise AttributeError(f'Item with name {element.name} already exists')

    def __setitem__(self, key, value):
        super(ShoppingListWithoutDuplicates, self).__setitem__(key, value)
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()

    def remove(self, item) -> None:
        super(ShoppingListWithoutDuplicates, self).remove(item)
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()

    def clear(self):
        super().clear()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()
