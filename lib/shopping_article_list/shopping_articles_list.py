from lib.lists.list_without_duplicates import ShoppingListWithoutDuplicates
from lib.shopping_article.shopping_article import ShoppingArticle


class ShoppingArticlesList(ShoppingListWithoutDuplicates):

    def __init__(self, shopping_categories):
        super().__init__()
        self.shopping_categories = shopping_categories

    def sort_by_article_name(self):
        self.sort(key=lambda x: x.name)

    def add_new_article(self, name: str, category: str) -> ShoppingArticle:
        article = ShoppingArticle(name, category)
        self.append(article)
        return article

    def get_article_by_name(self, name: str) -> ShoppingArticle:
        for article in self:
            if article.name == name:
                return article
        raise AttributeError(f'Article {name} not found')

    def remove_article(self, name: str):
        self.remove(self.get_article_by_name(name))
