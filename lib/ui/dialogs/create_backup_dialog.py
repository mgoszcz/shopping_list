
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton

from lib.backup_manager.backup_manager import BackupManager, AUTO_BACKUP_PREFIX
from lib.ui.widgets.buttons.cancel_button import CancelButton


class _BackupNameLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self._label = QLabel('Nazwa: ')
        self.name = QLineEdit()

        self.addWidget(self._label)
        self.addWidget(self.name)


class _CreateBackupButtonsLayout(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.ok_button = QPushButton('Ok')
        self.cancel_button = CancelButton()
        self.addWidget(self.ok_button)
        self.addWidget(self.cancel_button)


class CreateBackupDialog(QDialog):

    def __init__(self, backup_manager: BackupManager):
        super().__init__()
        self._backup_manager = backup_manager
        self._name_layout = _BackupNameLayout()
        self._buttons_layout = _CreateBackupButtonsLayout()
        self._layout = QVBoxLayout()
        self._layout.addLayout(self._name_layout)
        self._layout.addLayout(self._buttons_layout)
        self._triggered = False

        self.setLayout(self._layout)

        self.disable_button()

        self._buttons_layout.ok_button.pressed.connect(self.accept_button)
        self._buttons_layout.cancel_button.pressed.connect(self.reject)
        self._name_layout.name.textChanged.connect(self.disable_button)

    def disable_button(self):
        self._buttons_layout.ok_button.setDisabled(False)
        if self._name_layout.name.text().startswith(AUTO_BACKUP_PREFIX):
            self._buttons_layout.ok_button.setDisabled(True)
        if self._name_layout.name.text() in self._backup_manager.backups_list:
            self._buttons_layout.ok_button.setDisabled(True)
        if not self._name_layout.name.text():
            self._buttons_layout.ok_button.setDisabled(True)

    def accept_button(self):
        if not self._triggered:
            self._triggered = True
            backup_name = self._name_layout.name.text()
            self._backup_manager.create_backup(auto=False, file_name=backup_name)
            self.accept()

    def initialize(self):
        self._name_layout.name.clear()
        self.disable_button()
        self._triggered = False
