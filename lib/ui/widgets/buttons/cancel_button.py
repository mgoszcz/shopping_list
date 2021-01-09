from PyQt5.QtWidgets import QPushButton


class CancelButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Cancel')
