from lib.lists.list_without_duplicates import ShoppingListWithoutDuplicates
from lib.shopping_article.shopping_article import ShoppingArticle


class ShoppingListBase(ShoppingListWithoutDuplicates):

    def get_article_by_name(self, name: str) -> ShoppingArticle:
        for article in self:
            if article.name == name:
                return article
        raise AttributeError(f'Article {name} not found')

    def remove_article(self, name: str):
        self.remove(self.get_article_by_name(name))
