"""Module contains class ShoppingListInterface"""
from lib.backup_manager.backup_manager import BackupManager
from lib.save_load.save_load import SaveLoad, AutoSave
from lib.shop.shops_list import ShopsList
from lib.shopping_article_list.shopping_articles_list import ShoppingArticlesList
from lib.shopping_article_list.shopping_list import ShoppingList
from lib.shopping_categories.category_list import CategoryList


class ShoppingListInterface:
    """Implementation of shopping list interface"""
    def __init__(self):
        self.categories = CategoryList()
        self.shops = ShopsList(self.categories)
        self.shopping_articles = ShoppingArticlesList(self.categories, self.shops)
        self.shopping_list = ShoppingList(self.shopping_articles, self.shops)
        self._save_load = SaveLoad(self)
        self._save_load.load_data_from_server()
        self._auto_save = AutoSave(self._save_load)
        self._auto_save.start()
        self.backup_manager = BackupManager(self)
        self.backup_manager.create_backup(auto=True)
