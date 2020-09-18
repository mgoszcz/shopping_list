from lib.shop.shops_list import ShopsList
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.shopping_categories.category_list import CategoryList


class ShoppingListInterface:

    def __init__(self):
        self.categories = CategoryList()
        self.shopping_articles = ShoppingArticlesList(self.categories)
        self.shopping_list = ShoppingList(self.shopping_articles)
        self.shops = ShopsList()

    def add_new_article_to_shopping_list(self, name: str, category: str):
        article = self.shopping_list.add_new_article(name, category)
        self.shopping_articles.append(article)
        article.selection += 1
