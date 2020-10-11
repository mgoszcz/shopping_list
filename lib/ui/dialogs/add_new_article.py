from typing import Union

from PyQt5.QtWidgets import QDialog

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.layouts.add_article_dialog_layout import AddArticleDialogLayout


class AddNewArticleDialog(QDialog):

    def __init__(self, items_list: Union[ShoppingArticlesList, ShoppingList]):
        super(AddNewArticleDialog, self).__init__()
        self._items_list = items_list
        self.new_article = AddArticleDialogLayout()
        self.setLayout(self.new_article)
        self.new_article.buttonbox.rejected.connect(self.reject)
        self.new_article.buttonbox.accepted.connect(self.accept_button)

    def accept_button(self):
        article = self.new_article.product.text()
        category = self.new_article.category.text()
        self._items_list.add_new_article(article, category)
        self.accept()
