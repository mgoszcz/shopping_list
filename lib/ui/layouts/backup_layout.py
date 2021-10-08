"""
Contains BackupLayout class
"""
from PyQt5.QtWidgets import QHBoxLayout  # pylint: disable=no-name-in-module

from lib.backup_manager.backup_manager import BackupManager
from lib.ui.dialogs.backup_dialog import BackupDialog
from lib.ui.dialogs.create_backup_dialog import CreateBackupDialog
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.buttons.backup_button import BackupButton, CreateBackupButton


class BackupLayout(QHBoxLayout):
    """
    Implements backup layout on main window
    """
    def __init__(self, backup_manager: BackupManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.backup_button = BackupButton()
        self.create_backup_button = CreateBackupButton()

        self._backup_dialog = BackupDialog(backup_manager)
        self._create_backup_dialog = CreateBackupDialog(backup_manager)

        self.addWidget(self.backup_button)
        self.addWidget(self.create_backup_button)

        self.backup_button.pressed.connect(self.backup)
        self.create_backup_button.pressed.connect(self.create_user_backup)

    def backup(self):
        """
        Action when pressing backups button - will open dialog with backups
        """
        self._backup_dialog.layout.backup_list.populate_list()
        self._backup_dialog.exec_()
        LIST_SIGNALS.emit_all()

    def create_user_backup(self):
        """
        Action when pressing create backup button - will open dialog to create user backup
        """
        self._create_backup_dialog.initialize()
        self._create_backup_dialog.exec_()
