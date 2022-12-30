from lib.save_load.events import SAVE_NEEDED
from lib.shopping_article.shopping_article import ShoppingArticle


class ShoppingListItem:
    def __init__(self, shopping_article: ShoppingArticle, amount: int = 1, checked: bool = False):
        self.article = shopping_article
        self.amount = amount
        self.checked = checked

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        SAVE_NEEDED.set()
