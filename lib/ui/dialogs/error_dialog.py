"""
Module contains class ErrorDialog
"""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox  # pylint: disable=no-name-in-module


class ErrorDialog(QDialog):
    """
    Implementation of error dialog
    """
    def __init__(self, text: str):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(text))
        button = QDialogButtonBox.Ok
        buttonbox = QDialogButtonBox(button)
        layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        self.setLayout(layout)
