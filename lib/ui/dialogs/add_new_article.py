from PyQt5.QtWidgets import QDialog

from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.ui.layouts.add_article_dialog_layout import AddArticleDialogLayout


class AddNewArticleDialog(QDialog):

    def __init__(self, items_list: ShoppingArticlesList):
        super(AddNewArticleDialog, self).__init__()
        self._items_list = items_list
        self.new_article = AddArticleDialogLayout(self._items_list)
        self.article_name = None
        self.setLayout(self.new_article)
        self.disable_button()

        self.new_article.ok_button.pressed.connect(self.accept_button)
        self.new_article.cancel.pressed.connect(self.reject)
        self.new_article.product.textChanged.connect(self.disable_button)

    def accept_button(self):
        article = self.new_article.product.text()
        if not article:
            raise RuntimeError('Nie można dodać artykułu bez nazwy')
        try:
            self._items_list.get_article_by_name(article)
            raise RuntimeError(f'Article {article} already exists')
        except AttributeError:
            category = self.new_article.category.currentText()
            self._items_list.add_new_article(article, category)
            self.article_name = article
            self.accept()

    def disable_button(self):
        button = self.new_article.ok_button
        if self.new_article.product.text() == '':
            button.setDisabled(True)
            self.new_article.error.setText('Nie można dodać artykułu bez nazwy')
        elif self.new_article.product.text() in [x.name for x in self._items_list]:
            button.setDisabled(True)
            self.new_article.error.setText('Taki artykuł już istnieje')
        else:
            button.setDisabled(False)
            self.new_article.error.setText('')
