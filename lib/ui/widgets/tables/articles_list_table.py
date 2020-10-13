from lib.shopping_article.shopping_article import ShoppingArticle
from lib.ui.widgets.tables.base_table_widget import BaseTableWidget


class ArticlesListTableAlphabetical(BaseTableWidget):

    def _items_modifier(self):
        return self._items_list.sort_by_article_name()

    def _category_change(self, article: ShoppingArticle, new_value: str):
        self._items_list.edit_category(article, new_value)
