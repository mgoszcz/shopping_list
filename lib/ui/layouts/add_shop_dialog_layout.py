"""
Module contains class AddShopDialogLayout
"""
from pathlib import Path
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QLabel, QDialogButtonBox, \
    QHBoxLayout, QPushButton, QFileDialog  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class _LogoBrowser(QHBoxLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = QLineEdit()
        self.browser_button = QPushButton('Browse')
        self.addWidget(self.file_path)
        self.addWidget(self.browser_button)

        self.browser_button.pressed.connect(self.open_browser)

    def open_browser(self):
        """Open file browser to select logo file"""
        dialog = QFileDialog(caption='Open Image', directory=str(Path.home()), filter='Image Files (*.png *.jpg *.bmp)')
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        if dialog.exec_():
            self.file_path.setText(dialog.selectedFiles()[0])


class AddShopDialogLayout(QGridLayout):
    """
    Layout for add shop dialog
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_SHOP_DIALOG_LAYOUT)
        self.name = QLineEdit()
        self.logo = _LogoBrowser()
        self.addWidget(QLabel('Nazwa: '), 0, 0)
        self.addWidget(self.name, 0, 1)
        self.addWidget(QLabel('Logo: '), 1, 0)
        self.addLayout(self.logo, 1, 1)
        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonbox = QDialogButtonBox(btn)
        self.addWidget(self.buttonbox, 2, 1)
