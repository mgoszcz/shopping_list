from PyQt5.QtWidgets import QPushButton


class ArticleListButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Lista artykułów')
