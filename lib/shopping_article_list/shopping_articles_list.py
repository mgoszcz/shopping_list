from typing import List

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_list_base import ShoppingListBase
from lib.shopping_categories.category_list import CategoryList


class ShoppingArticlesList(ShoppingListBase):

    def __init__(self, shopping_categories: CategoryList):
        super().__init__()
        self.shopping_categories = shopping_categories

    def append(self, element: ShoppingArticle) -> None:
        super().append(element)
        self.shopping_categories.append(element.category)

    def sort_by_article_name(self):
        return sorted(self, key=lambda x: x.name)

    def add_new_article(self, name: str, category: str) -> ShoppingArticle:
        article = ShoppingArticle(name, category)
        self.append(article)
        return article

    def print_names_and_categories(self) -> List[str]:
        if not self:
            return []
        article_length = len(max([x.name for x in self], key=len)) + 5
        category_length = len(max([x.category for x in self], key=len))
        return [f'{x.name:{article_length}}|{"":5}{x.category:{category_length}}' for x in self]
