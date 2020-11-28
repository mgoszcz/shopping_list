from typing import List

from lib.shop.shops_list import ShopsList
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_list_base import ShoppingListBase
from lib.shopping_categories.category_list import CategoryList


class ShoppingArticlesList(ShoppingListBase):

    def __init__(self, shopping_categories: CategoryList, shops: ShopsList):
        super().__init__()
        self.shopping_categories = shopping_categories
        self._shops = shops

    def _remove_if_unused_category(self, category):
        if category not in [article.category for article in self]:
            self.shopping_categories.remove(category)
            for shop in self._shops:
                if category in shop.category_list:
                    shop.category_list.remove(category)

    def append(self, element: ShoppingArticle) -> None:
        super().append(element)
        self.shopping_categories.append(element.category)

    def remove(self, item: ShoppingArticle):
        category = item.category
        super().remove(item)
        self._remove_if_unused_category(category)

    def sort_by_article_name(self):
        return sorted(self, key=lambda x: x.name)

    def add_new_article(self, name: str, category: str) -> ShoppingArticle:
        article = ShoppingArticle(name, category)
        self.append(article)
        return article

    def edit_category(self, article: ShoppingArticle, new_category: str):
        if new_category not in self.shopping_categories:
            self.shopping_categories.append(new_category)
        old_category = article.category
        article.category = new_category
        self._remove_if_unused_category(old_category)

    def clear(self):
        super().clear()
        self.shopping_categories.clear()
