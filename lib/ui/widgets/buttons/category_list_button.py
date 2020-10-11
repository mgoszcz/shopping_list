from PyQt5.QtWidgets import QPushButton


class CategoryListButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Kategorie')
