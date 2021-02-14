from PyQt5.QtWidgets import QPushButton


class BackupButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Backups')


class CreateBackupButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setText('Dodaj backup')
