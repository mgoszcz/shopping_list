from PyQt5.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QLabel  # pylint: disable=no-name-in-module


class ConfirmDialog(QDialog):

    def __init__(self, text: str):
        super().__init__()
        layout = QVBoxLayout()
        btn = QDialogButtonBox.Yes | QDialogButtonBox.No
        self.buttonbox = QDialogButtonBox(btn)
        layout.addWidget(QLabel(text))
        layout.addWidget(self.buttonbox)
        self.setLayout(layout)
        self.buttonbox.rejected.connect(self.reject)
        self.buttonbox.accepted.connect(self.accept)
