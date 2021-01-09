from PyQt5.QtWidgets import QPushButton


class RevertButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Revert')
