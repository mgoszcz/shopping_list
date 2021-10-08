"""
Module contains BackupListWidget class
"""
from PyQt5.QtWidgets import QListWidget  # pylint: disable=no-name-in-module

from lib.backup_manager.backup_manager import BackupManager
from lib.ui.object_names.object_names import ObjectNames


class BackupListWidget(QListWidget):
    """
    Implements backups list widget
    """
    def __init__(self, backup_manager: BackupManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.BACKUP_LIST_WIDGET)
        self._backup_manager = backup_manager

        self.populate_list()

    def populate_list(self):
        """
        Populate backups list widget
        """
        self.clear()
        self.addItems(self._backup_manager.backups_list)
