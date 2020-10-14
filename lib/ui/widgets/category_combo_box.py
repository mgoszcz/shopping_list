from PyQt5.QtWidgets import QComboBox

from lib.shopping_categories.category_list import CategoryList


class CategoryComboBox(QComboBox):
    def __init__(self, category_list: CategoryList):
        super().__init__()
        self.items = category_list

        self._populate_list()
        self.setEditable(True)

    def _populate_list(self):
        for i in reversed(range(1, self.count())):
            self.removeItem(i)
        self.addItems([x for x in self.items])