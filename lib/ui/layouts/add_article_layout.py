from PyQt5.QtWidgets import QHBoxLayout

from lib.shopping_article_list.shopping_list import ShoppingList
from lib.ui.signals.list_signals import LIST_SIGNALS
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

        self.disable_button_when_item_added()

        self._add_button.pressed.connect(self.add_article_to_list)
        self._article_combo_box.activated.connect(self.disable_button_when_item_added)
        LIST_SIGNALS.list_changed.connect(self.disable_button_when_item_added)

    def add_article_to_list(self):
        article = self._article_combo_box.get_current_article()
        self._shopping_list.add_existing_article(article)
        self.disable_button_when_item_added()

    def disable_button_when_item_added(self):
        if self._article_combo_box.currentIndex() <= 0:
            self._add_button.setDisabled(True)
        else:
            if self._article_combo_box.get_current_article() in self._shopping_list:
                self._add_button.setDisabled(True)
            else:
                self._add_button.setDisabled(False)
