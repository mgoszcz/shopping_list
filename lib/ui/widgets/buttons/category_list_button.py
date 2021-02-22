from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class CategoryListButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Kategorie')
