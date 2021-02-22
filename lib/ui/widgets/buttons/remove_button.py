from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class RemoveButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Usuń')
