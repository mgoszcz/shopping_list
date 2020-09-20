from lib.shop.shop import Shop
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list_base import ShoppingListBase


class ShoppingList(ShoppingListBase):

    def __init__(self, shopping_articles_list: ShoppingArticlesList):
        super().__init__()
        self.shopping_articles_list = shopping_articles_list
        self.selected_shop: Shop = None

    def sort_by_shop(self):
        raise NotImplementedError

    def add_existing_article(self, element: ShoppingArticle):
        self.append(element)
        element.selection += 1

    def add_new_article(self, name: str, category: str) -> ShoppingArticle:
        article = ShoppingArticle(name, category)
        self.append(article)
        self.shopping_articles_list.append(article)
        return article
