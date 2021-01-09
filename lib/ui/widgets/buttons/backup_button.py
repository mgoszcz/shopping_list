from PyQt5.QtWidgets import QPushButton


class BackupButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Backup')