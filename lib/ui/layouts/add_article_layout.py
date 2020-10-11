from PyQt5.QtWidgets import QHBoxLayout

from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.combo_box import ArticleComboBox


class AddArticleLayout(QHBoxLayout):

    def __init__(self, shopping_list: ShoppingList):
        super().__init__()
        self._shopping_list = shopping_list
        self._article_combo_box = ArticleComboBox(self._shopping_list.shopping_articles_list)
        self._add_button = AddButton()
        self.addWidget(self._article_combo_box)
        self.addWidget(self._add_button)

        self._add_button.pressed.connect(self.add_article_to_list)

    def add_article_to_list(self):
        article = self._article_combo_box.get_current_article()
        self._shopping_list.add_existing_article(article)
