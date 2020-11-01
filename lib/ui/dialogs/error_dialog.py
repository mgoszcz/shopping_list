from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox


class ErrorDialog(QDialog):
    def __init__(self, text: str):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(text))
        button = QDialogButtonBox.Ok
        buttonbox = QDialogButtonBox(button)
        layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        self.setLayout(layout)
