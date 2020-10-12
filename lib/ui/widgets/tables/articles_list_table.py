from lib.ui.widgets.tables.base_table_widget import BaseTableWidget


class ArticlesListTableAlphabetical(BaseTableWidget):

    def _items_modifier(self):
        return self._items_list.sort_by_article_name()
