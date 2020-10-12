from lib.ui.widgets.tables.base_table_widget import BaseTableWidget


class ShoppingListTable(BaseTableWidget):

    def _amount_changed(self):
        if self.currentColumn() == 2:
            article = self._items_list[self.currentRow()]
            article.amount = int(self.currentItem().text())
