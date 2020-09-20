from lib.shop.shop import Shop
from lib.shop.shops_list import ShopsList
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list_base import ShoppingListBase


class ShoppingList(ShoppingListBase):

    def __init__(self, shopping_articles_list: ShoppingArticlesList, shops_list: ShopsList):
        super().__init__()
        self.shopping_articles_list = shopping_articles_list
        self._shops_list = shops_list

    def sort_by_shop(self):
        ordered_items = []
        for category in self._shops_list.selected_shop.category_list:
            for item in self:
                if item.category == category:
                    index = self.index(item)
                    self.pop(index)
                    self.append(item)
                    ordered_items.append(item)

    def add_existing_article(self, element: ShoppingArticle):
        self.append(element)
        element.selection += 1

    def add_new_article(self, name: str, category: str) -> ShoppingArticle:
        article = ShoppingArticle(name, category)
        self.append(article)
        self.shopping_articles_list.append(article)
        return article
