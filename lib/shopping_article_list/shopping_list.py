from lib.save_load.events import SAVE_NEEDED
from lib.shop.shops_list import ShopsList
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list_base import ShoppingListBase
from lib.ui.signals.list_signals import LIST_SIGNALS


class ShoppingList(ShoppingListBase):

    def __init__(self, shopping_articles_list: ShoppingArticlesList, shops_list: ShopsList):
        super().__init__()
        self.shopping_articles_list = shopping_articles_list
        self._shops_list = shops_list
        self.unordered_items = []

    def sort_by_shop(self):
        ordered_items = []
        sorted_list = sorted(self, key=lambda x: x.name)
        for category in self._shops_list.selected_shop.category_list:
            for item in sorted_list:
                if item.category == category:
                    ordered_items.append(item)
        self.unordered_items = [item for item in sorted_list if item not in ordered_items]
        self.clear_silent()
        for item in self.unordered_items + ordered_items:
            self.append_silent(item)

    def add_existing_article(self, element: ShoppingArticle):
        self.append_silent(element)
        element.selection += 1
        self.sort_by_shop()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()

    def add_new_article(self, name: str, category: str) -> ShoppingArticle:
        article = ShoppingArticle(name, category)
        self.append_silent(article)
        self.shopping_articles_list.append(article)
        self.sort_by_shop()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()
        return article

    def remove_article(self, name: str):
        self.remove_silent(self.get_article_by_name(name))
        self.sort_by_shop()
        SAVE_NEEDED.set()
        LIST_SIGNALS.list_changed.emit()
