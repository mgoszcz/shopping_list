from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.widgets.tables.base_table_widget import BaseTableWidget


class ShoppingListTable(BaseTableWidget):

    def _amount_changed(self, article: ShoppingArticle, new_value: str) -> bool:
        article.amount = new_value
        return True

    def _category_change(self, article: ShoppingArticle, new_value: str) -> bool:
        self._items_list.shopping_articles_list.edit_category(article, new_value)
        return True

    def _action_if_existing_article(self, article: ShoppingArticle, shopping_list: ShoppingList,
                                    new_value: str) -> bool:
        try:
            print(new_value)
            new_article = shopping_list.shopping_articles_list.get_article_by_name(new_value)
            print(new_article)
            shopping_list.remove(article)
            shopping_list.append(new_article)
            return True
        except AttributeError:
            return False

    def _action_if_non_existing_article(self, article: ShoppingArticle, shopping_list: ShoppingList,
                                        new_value: str) -> bool:
        shopping_list.add_new_article(new_value, article.category)
        shopping_list.remove(article)
        return True
