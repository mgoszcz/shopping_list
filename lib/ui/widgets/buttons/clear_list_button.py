from PyQt5.QtWidgets import QPushButton


class ClearListButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Wyczyść')
