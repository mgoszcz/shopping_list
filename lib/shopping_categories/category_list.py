from lib.lists.list_without_duplicates import StringListWithoutDuplicates
from lib.save_load.events import SAVE_NEEDED
from lib.ui.signals.list_signals import LIST_SIGNALS


class CategoryList(StringListWithoutDuplicates):

    def move_up(self, element: str):
        index = self.index(element)
        if index == 0:
            raise AttributeError(f'Attribute {element} is already at the top of the list')
        self[index] = self[index - 1]
        self[index - 1] = element
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()

    def move_down(self, element: str):
        index = self.index(element)
        if index == len(self) - 1:
            raise AttributeError(f'Attribute {element} is already at the bottom of the list')
        self[index] = self[index + 1]
        self[index + 1] = element
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()


