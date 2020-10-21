from PyQt5.QtWidgets import QPushButton


class MoveUpButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('\u2191')


class MoveDownButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('\u2193')
