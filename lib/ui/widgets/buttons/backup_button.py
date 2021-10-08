"""
Module contains classes BackupButton and CreateBackupButton
"""
from PyQt5.QtWidgets import QPushButton  # pylint: disable=no-name-in-module


class BackupButton(QPushButton):
    """
    Implements Backup button to open backups dialog
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Punkty przywracania')


class CreateBackupButton(QPushButton):
    """
    Implements create backup button to create user backup
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Utwórz punkt przywracania')
