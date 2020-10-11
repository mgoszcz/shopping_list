from PyQt5.QtWidgets import QPushButton


class AddButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Dodaj')
