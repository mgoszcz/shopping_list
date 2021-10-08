"""
Module contains class ErrorDialog
"""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox  # pylint: disable=no-name-in-module

from lib.ui.icons.icons import ErrorIcon


class ErrorDialog(QDialog):
    """
    Implementation of error dialog
    """
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Błąd!')
        self.setWindowIcon(ErrorIcon.q_icon())
        layout = QVBoxLayout()
        layout.addWidget(QLabel(text))
        button = QDialogButtonBox.Ok
        buttonbox = QDialogButtonBox(button)
        layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        self.setLayout(layout)
