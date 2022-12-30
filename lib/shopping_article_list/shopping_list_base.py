"""Contains class ShoppingListBase"""
from lib.lists.list_without_duplicates import ShopAndArticleListWithoutDuplicates
from lib.shopping_article.shopping_article import ShoppingArticle


class ShoppingListBase(ShopAndArticleListWithoutDuplicates):
    """Implementation of base list object used by shopping list and shopping articles list"""
    def get_article_by_name(self, name: str) -> ShoppingArticle:
        """
        Get article with specific name from list
        :param name: Name of article
        """
        for article in self:
            if article.name == name:
                return article
        raise AttributeError(f'Article {name} not found')

    def remove_article(self, name: str):
        """
        Remove article from list
        :param name: Name of article
        """
        self.remove(self.get_article_by_name(name))
