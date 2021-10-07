"""
Module contains class ArticlesDialog
"""
from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.dialogs.add_new_article import AddNewArticleDialog
from lib.ui.dialogs.confirm_dialog import ConfirmDialog
from lib.ui.dialogs.error_dialog import ErrorDialog
from lib.ui.icons.icons import ShoppingListIcon
from lib.ui.layouts.articles_dialog_layout import ArticlesDialogLayout


class ArticlesDialog(QDialog):
    """
    Implementation of articles list dialog
    """
    def __init__(self, items_list: ShoppingList):
        super().__init__()
        self._items_list = items_list
        self.setWindowTitle('Baza artykułów')
        self.setWindowIcon(ShoppingListIcon.q_icon())
        self.layout = ArticlesDialogLayout(self._items_list)
        self.setLayout(self.layout)

        self.layout.add_button.pressed.connect(self.add_article)
        self.layout.add_to_shopping_list_button.pressed.connect(self.add_article_to_list)
        self.layout.remove_button.pressed.connect(self.remove_article)
        self.layout.clear_list_button.pressed.connect(self.clear_article_list)

    def add_article(self):
        """
        Action on pressing add article button - opens add articles dialog
        """
        dialog = AddNewArticleDialog(self._items_list.shopping_articles_list)
        dialog.exec_()

    def remove_article(self):
        """
        Action on pressing remove article button - Removes article (requires user confirmation)
        """
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
        """
        Action on pressing clear list button - clears articles list (requires user confirmation)
        """
        dialog = ConfirmDialog('Czy jesteś pewien aby wyczyścić listę artykułów?\nWyczyszczona zostanie rónież lista '
                               'zakupów')
        if dialog.exec_():
            self._items_list.shopping_articles_list.clear()
            self._items_list.clear()

    def add_article_to_list(self):
        """Method handles adding article to shopping list when pressing button"""
        if not self.layout.articles_table.item(self.layout.articles_table.currentRow(), 0):
            dialog = ErrorDialog('Wybierz artykuł!')
            dialog.exec_()
            return
        article_name = self.layout.articles_table.item(self.layout.articles_table.currentRow(), 0).text()
        article = self.layout.articles_table.items_list.get_article_by_name(article_name)
        if article in self._items_list:
            dialog = ErrorDialog('Artykuł już jest na liscie')
            dialog.exec_()
            return
        if article:
            self._items_list.append(article)
        else:
            raise Exception('Undefined state when adding article to list')
