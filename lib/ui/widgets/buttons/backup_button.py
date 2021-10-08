"""
Module contains classes BackupButton and CreateBackupButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames


class BackupButton(QPushButton):
    """
    Implements Backup button to open backups dialog
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.BACKUP_BUTTON)
        self.setText('Punkty przywracania')


class CreateBackupButton(QPushButton):
    """
    Implements create backup button to create user backup
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CREATE_BACKUP_BUTTON)
        self.setText('Utwórz punkt przywracania')
