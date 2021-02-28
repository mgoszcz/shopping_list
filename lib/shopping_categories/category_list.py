"""
Module contains class CategoryList
"""
from lib.lists.list_without_duplicates import StringListWithoutDuplicates
from lib.save_load.events import SAVE_NEEDED
from lib.ui.signals.list_signals import LIST_SIGNALS


class CategoryList(StringListWithoutDuplicates):
    """
    Implementation of category list, contains method to move list items up and down
    """
    def move_up(self, element: str):
        """
        Move category one level up (move item on list to preceding index). Raise error when current index is 0
        :param element: List element to be moved
        """
        index = self.index(element)
        if index == 0:
            raise AttributeError(f'Attribute {element} is already at the top of the list')
        self[index] = self[index - 1]
        self[index - 1] = element
        self.custom_sort = True
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()

    def move_down(self, element: str):
        """
        Move category one level down (move item on list to following index). Raise error when current index is -1
        :param element: List element to be moved
        """
        index = self.index(element)
        if index == len(self) - 1:
            raise AttributeError(f'Attribute {element} is already at the bottom of the list')
        self[index] = self[index + 1]
        self[index + 1] = element
        self.custom_sort = True
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()

    def move_top(self, element: str):
        """
        Move category to top (move item on list to 0 index). Raise error when current index is 0
        :param element: List element to be moved
        """
        index = self.index(element)
        if index == 0:
            raise AttributeError(f'Attribute {element} is already at the top of the list')
        self.insert(0, self.pop(index))
        self.custom_sort = True
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()

    def move_bottom(self, element: str):
        """
        Move category to bottom (move item on list to last). Raise error when current index is -1
        :param element: List element to be moved
        """
        index = self.index(element)
        if index == len(self) - 1:
            raise AttributeError(f'Attribute {element} is already at the bottom of the list')
        self.append(self.pop(index))
        self.custom_sort = True
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()
