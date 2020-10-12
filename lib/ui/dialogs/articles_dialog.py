from PyQt5.QtWidgets import QDialog, QVBoxLayout

from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.layouts.articles_dialog_layout import ArticlesDialogLayout
from lib.ui.widgets.tables.articles_list_table import ArticlesListTableAlphabetical


class ArticlesDialog(QDialog):
    def __init__(self, items_list: ShoppingList):
        super().__init__()
        self._items_list = items_list
        self.layout = ArticlesDialogLayout(self._items_list.shopping_articles_list)
        self.setLayout(self.layout)

        self.layout.add_button.pressed.connect(self.add_article)
        self.layout.remove_button.pressed.connect(self.remove_article)
        self.layout.clear_list_button.pressed.connect(self.clear_article_list)

    def add_article(self):
        dialog = AddNewArticleDialog(self._items_list.shopping_articles_list)
        dialog.exec_()

    def remove_article(self):
        article = self.layout.articles_table.item(self.layout.articles_table.currentRow(), 0).text()
        self._items_list.shopping_articles_list.remove_article(article)
        try:
            self._items_list.get_article_by_name(article)
            # TODO: DIALOG
            print('DIALOG DO WYWALANIA 1')
            self._items_list.remove_article(article)
        except AttributeError:
            pass

    def clear_article_list(self):
        # TODO: DIALOG
        print('DIALOG CZY NA PEWNO 1')
        self._items_list.shopping_articles_list.clear()
        self._items_list.clear()