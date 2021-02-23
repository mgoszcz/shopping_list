"""
Module contains class ArticlesListTableAlphabetical
"""
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.widgets.tables.base_table_widget import BaseTableWidget


class ArticlesListTableAlphabetical(BaseTableWidget):
    """
    Implementation of alphabetically ordered articles list table widget
    """
    def _items_modifier(self):
        return self._items_list.sort_by_article_name()

    def _category_change(self, article: ShoppingArticle, new_value: str) -> bool:
        self._items_list.edit_category(article, new_value)
        return True

    def _action_if_non_existing_article(self, article: ShoppingArticle, shopping_list: ShoppingList,
                                        new_value: str) -> bool:
        article.name = new_value
        return True

    def _action_if_existing_article(self, article: ShoppingArticle, shopping_list: ShoppingList, new_value: str):
        raise NotImplementedError

    def _amount_changed(self, article: ShoppingArticle, new_value: str):
        raise NotImplementedError
