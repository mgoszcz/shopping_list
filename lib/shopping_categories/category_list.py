

class CategoryList(set):

    def add(self, element: str) -> None:
        super().add(element.lower())
