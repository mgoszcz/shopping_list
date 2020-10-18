from PyQt5.QtWidgets import QGridLayout, QLineEdit, QLabel, QDialogButtonBox


class AddShopDialogLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        self.name = QLineEdit()
        self.logo = QLabel('<logo>')
        self.addWidget(QLabel('Nazwa: '), 0, 0)
        self.addWidget(self.name, 0, 1)
        self.addWidget(QLabel('Logo: '), 1, 0)
        self.addWidget(self.logo, 1, 1)
        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonbox = QDialogButtonBox(btn)
        self.addWidget(self.buttonbox, 2, 1)
