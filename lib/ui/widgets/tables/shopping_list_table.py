from lib.shopping_article.shopping_article import ShoppingArticle
from lib.ui.widgets.tables.base_table_widget import BaseTableWidget


class ShoppingListTable(BaseTableWidget):

    def _amount_changed(self, article: ShoppingArticle, new_value: str):
        article.amount = new_value

    def _category_change(self, article: ShoppingArticle, new_value: str):
        self._items_list.shopping_articles_list.edit_category(article, new_value)