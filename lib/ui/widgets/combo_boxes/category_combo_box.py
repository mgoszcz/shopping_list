"""
Module contains class CategoryComboBox
"""
from PyQt5.QtWidgets import QComboBox  # pylint: disable=no-name-in-module

from lib.shopping_categories.category_list import CategoryList
from lib.ui.object_names.object_names import ObjectNames


class CategoryComboBox(QComboBox):
    """
    Implementation of combo box to select categories in shop's category dialog box
    """
    def __init__(self, category_list: CategoryList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CATEGORY_COMBO_BOX)
        self.items = category_list

        self._populate_list()
        self.setEditable(True)

    def _populate_list(self):
        for i in reversed(range(1, self.count())):
            self.removeItem(i)
        self.addItems(self.items)
