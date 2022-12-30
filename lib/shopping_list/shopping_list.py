"""Module contains Shopping list"""

from lib.lists.list_without_duplicates import ShoppingListWithoutDuplicates
from lib.save_load.events import SAVE_NEEDED
from lib.shop.shops_list import ShopsList
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_list.shopping_list_item import ShoppingListItem
from lib.ui.signals.list_signals import LIST_SIGNALS


class ShoppingList(ShoppingListWithoutDuplicates):
    """Implementation of shopping list logic"""

    def __init__(self, shopping_articles_list: ShoppingArticlesList, shops_list: ShopsList):
        super().__init__()
        self.shopping_articles_list = shopping_articles_list
        self._shops_list = shops_list
        self.unordered_items = []

    def get_item_by_article_name(self, name: str) -> ShoppingListItem:
        """
        Get item with specific article from list
        :param name: Name of article
        """
        for item in self:
            if item.article.name == name:
                return item
        raise AttributeError(f'Article {name} not found')

    def get_article_by_name(self, name: str) -> ShoppingArticle:
        """
        Get item with specific article from list
        :param name: Name of article
        """
        for item in self:
            if item.article.name == name:
                return item.article
        raise AttributeError(f'Article {name} not found')

    def sort_by_shop(self):
        """Sort items on shopping list by categories in category list for current shop"""
        ordered_items = []
        sorted_list = sorted(self, key=lambda x: x.article.name)
        if self._shops_list.selected_shop:
            for category in self._shops_list.selected_shop.category_list:
                for item in sorted_list:
                    if item.article.category == category:
                        ordered_items.append(item)
        else:
            ordered_items = sorted_list[:]
        self.unordered_items = [item for item in sorted_list if item not in ordered_items]
        self.clear_silent()
        for item in self.unordered_items + ordered_items:
            self.append_silent(item)

    def add_existing_article(self, element: ShoppingArticle):
        """Add article from articles list to shopping list (save and refresh GUI)"""
        self.append_silent(ShoppingListItem(element))
        element.selection += 1
        self.sort_by_shop()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()

    def add_new_article(self, name: str, category: str, amount: int = 1, checked: bool = False) -> ShoppingArticle:
        """
        Add new article with article object creation, adding new article to articles list and shopping list
        (save and refresh GUI)
        """
        article = ShoppingArticle(name, category)
        self.append_silent(ShoppingListItem(article, amount, checked))
        self.shopping_articles_list.append(article)
        article.selection += 1
        self.sort_by_shop()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()
        return article

    def remove_article(self, name: str):
        """Remove article from shopping list (save and refresh GUI)"""
        self.remove_silent(self.get_item_by_article_name(name))
        self.sort_by_shop()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()
