"""
Module contains class CategoryListWidget
"""
from PyQt5.QtWidgets import QListWidget  # pylint: disable=no-name-in-module

from lib.shopping_categories.category_list import CategoryList
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.list_signals import LIST_SIGNALS


class CategoryListWidget(QListWidget):
    """
    Implementation of category list widget used in category dialog
    """
    def __init__(self, category_list: CategoryList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CATEGORY_LIST_WIDGET)
        self._category_list = category_list

        self._populate_list()

        LIST_SIGNALS.category_list_changed.connect(self._populate_list)

    def _populate_list(self):
        self.clear()
        self.addItems(self._category_list)
