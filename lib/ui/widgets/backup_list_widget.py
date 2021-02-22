from PyQt5.QtWidgets import QListWidget  # pylint: disable=no-name-in-module

from lib.backup_manager.backup_manager import BackupManager


class BackupListWidget(QListWidget):
    def __init__(self, backup_manager: BackupManager):
        super().__init__()
        self._backup_manager = backup_manager

        self.populate_list()

    def populate_list(self):
        self.clear()
        self.addItems([x for x in self._backup_manager.backups_list])
