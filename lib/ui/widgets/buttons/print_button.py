from PyQt5.QtWidgets import QPushButton


class PrintButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Drukuj')