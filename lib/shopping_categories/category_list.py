from lib.lists.list_without_duplicates import StringListWithoutDuplicates


class CategoryList(StringListWithoutDuplicates):

    def move_up(self, element: str):
        index = self.index(element)
        if index == 0:
            raise AttributeError(f'Attribute {element} is already at the top of the list')
        self[index] = self[index - 1]
        self[index - 1] = element

    def move_down(self, element: str):
        index = self.index(element)
        if index == len(self) - 1:
            raise AttributeError(f'Attribute {element} is already at the bottom of the list')
        self[index] = self[index + 1]
        self[index + 1] = element


