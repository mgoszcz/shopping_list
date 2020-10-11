from PyQt5.QtWidgets import QPushButton


class RemoveButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Usuń')
