from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.dialogs.confirm_dialog import ConfirmDialog
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
        if article in [a.name for a in self._items_list]:
            text = 'Czy jesteś pewien aby usunąć artykuł?\nArtykuł zostanie również usunięty z listy zakupowej'
        else:
            text = 'Czy jesteś pewien aby usunąć artykuł?'
        dialog = ConfirmDialog(text)
        if dialog.exec_():
            self._items_list.shopping_articles_list.remove_article(article)
            try:
                self._items_list.get_article_by_name(article)
                self._items_list.remove_article(article)
            except AttributeError:
                pass

    def clear_article_list(self):
        dialog = ConfirmDialog('Czy jesteś pewien aby wyczyścić listę artykułów?\nWyczyszczona zostanie rónież lista '
                               'zakupów\nJest to nieodwracalna akcja')
        if dialog.exec_():
            self._items_list.shopping_articles_list.clear()
            self._items_list.clear()