"""
Module contains class AddShopDialogLayout
"""
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QLabel, QDialogButtonBox  # pylint: disable=no-name-in-module


class AddShopDialogLayout(QGridLayout):
    """
    Layout for add shop dialog
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = QLineEdit()
        self.logo = QLabel('<logo>')
        self.addWidget(QLabel('Nazwa: '), 0, 0)
        self.addWidget(self.name, 0, 1)
        self.addWidget(QLabel('Logo: '), 1, 0)
        self.addWidget(self.logo, 1, 1)
        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonbox = QDialogButtonBox(btn)
        self.addWidget(self.buttonbox, 2, 1)
