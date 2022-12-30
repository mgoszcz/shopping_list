"""
Module contains class ArticlesListTableAlphabetical
"""
from typing import List, Union

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_list.shopping_list import NewShoppingList
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.widgets.tables.base_table_widget import BaseTableWidget


class ArticlesListTableAlphabetical(BaseTableWidget):
    """
    Implementation of alphabetically ordered articles list table widget
    """
    def __init__(self, items_list: Union[NewShoppingList, ShoppingArticlesList], columns_count: int, *args, **kwargs):
        super().__init__(items_list, columns_count, *args, **kwargs)
        self.setObjectName(ObjectNames.ARTICLES_LIST_TABLE)

    def _items_modifier(self):
        return self.items_list.sort_by_article_name()

    def _category_change(self, article: ShoppingArticle, new_value: str) -> bool:
        self.items_list.edit_category(article, new_value)
        return True

    def _action_if_non_existing_article(self, article: ShoppingArticle, shopping_list: NewShoppingList,
                                        new_value: str) -> bool:
        article.name = new_value
        return True

    def _action_if_existing_article(self, article: ShoppingArticle, shopping_list: NewShoppingList, new_value: str):
        raise NotImplementedError

    def _amount_changed(self, article: ShoppingArticle, new_value: str):
        raise NotImplementedError

    def filter_articles(self, articles: Union[ShoppingArticlesList, List[ShoppingArticle]]):
        """Update table content"""
        self.items_list = articles
        self.populate_table()
