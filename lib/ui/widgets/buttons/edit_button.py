from PyQt5.QtWidgets import QPushButton


class EditButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Edytuj')
