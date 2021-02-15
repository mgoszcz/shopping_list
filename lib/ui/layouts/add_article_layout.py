"""
Contains class AddArticleLayout
"""

from PyQt5.QtWidgets import QHBoxLayout # pylint: disable=no-name-in-module

from lib.shopping_article.shopping_article import ShoppingArticle
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.combo_boxes.combo_box import ArticleComboBox


class AddArticleLayout(QHBoxLayout):
    """
    Class hold layout for add article widgets
    """

    def __init__(self, shopping_list: ShoppingList):
        super().__init__()
        self._shopping_list = shopping_list
        self._article_combo_box = ArticleComboBox(self._shopping_list.shopping_articles_list)
        self.add_button = AddButton()
        self.addWidget(self._article_combo_box)
        self.addWidget(self.add_button)

        self.disable_button_when_item_added()

        self._article_combo_box.activated.connect(self.disable_button_when_item_added)
        LIST_SIGNALS.list_changed.connect(self.disable_button_when_item_added)

    def add_article_to_list(self) -> ShoppingArticle:
        """
        Add to shopping list article selected in list box
        :return: article added
        """
        article = self._article_combo_box.get_current_article()
        self._shopping_list.add_existing_article(article)
        self.disable_button_when_item_added()
        return article

    def disable_button_when_item_added(self):
        """
        Disable add button if item is already added to shopping list
        """
        if self._article_combo_box.currentIndex() <= 0:
            self.add_button.setDisabled(True)
        else:
            if self._article_combo_box.get_current_article() in self._shopping_list:
                self.add_button.setDisabled(True)
            else:
                self.add_button.setDisabled(False)
