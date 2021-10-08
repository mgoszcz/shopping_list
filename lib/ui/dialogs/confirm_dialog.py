"""
Module contains class ConfirmDialog
"""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QLabel  # pylint: disable=no-name-in-module

from lib.ui.icons.icons import QuestionIcon


class ConfirmDialog(QDialog):
    """
    Implementation of confirm dialog (Yes/No)
    """
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Potwierdź...')
        self.setWindowIcon(QuestionIcon.q_icon())
        layout = QVBoxLayout()
        btn = QDialogButtonBox.Yes | QDialogButtonBox.No
        self.buttonbox = QDialogButtonBox(btn)
        layout.addWidget(QLabel(text))
        layout.addWidget(self.buttonbox)
        self.setLayout(layout)
        self.buttonbox.rejected.connect(self.reject)
        self.buttonbox.accepted.connect(self.accept)
