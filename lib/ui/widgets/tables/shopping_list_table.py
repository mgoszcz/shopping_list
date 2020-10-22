from typing import Union

from PyQt5.QtGui import QColor

from lib.save_load.events import AUTO_SAVE_PAUSED
from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.tables.base_table_widget import BaseTableWidget

UNORDERED_COLOR = QColor(255, 150, 150)

class ShoppingListTable(BaseTableWidget):

    def __init__(self, items_list: Union[ShoppingList, ShoppingArticlesList], columns_count: int):
        super().__init__(items_list, columns_count)
        LIST_SIGNALS.shop_changed.connect(self._shop_changed)
        LIST_SIGNALS.category_list_changed.connect(self._category_list_changed)

    def _color_unordered_rows(self):
        for i in range(self.rowCount()):
            if self.item(i, 0).text() in [x.name for x in self._items_list.unordered_items]:
                for j in range(3):
                    self.item(i, j).setBackground(UNORDERED_COLOR)

    def _shop_changed(self):
        self._items_list.sort_by_shop()
        LIST_SIGNALS.list_changed.emit()

    def _amount_changed(self, article: ShoppingArticle, new_value: str) -> bool:
        article.amount = new_value
        return True

    def _category_change(self, article: ShoppingArticle, new_value: str) -> bool:
        self._items_list.shopping_articles_list.edit_category(article, new_value)
        return True

    def _action_if_existing_article(self, article: ShoppingArticle, shopping_list: ShoppingList,
                                    new_value: str) -> bool:
        try:
            new_article = shopping_list.shopping_articles_list.get_article_by_name(new_value)
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

    def _category_list_changed(self):
        self._items_list.sort_by_shop()
        LIST_SIGNALS.list_changed.emit()
