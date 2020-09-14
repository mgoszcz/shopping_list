from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList


class ShoppingList(ShoppingArticlesList):

    def sort_by_shop(self):
        raise NotImplementedError

    def add_existing_article(self, element: ShoppingArticle):
        self.append(element)
        element.selection += 1
