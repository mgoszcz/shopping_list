"""
Module contains classes _BackupDialogButtonsLayout and BackupDialogLayout
"""
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout  # pylint: disable=no-name-in-module

from lib.backup_manager.backup_manager import BackupManager
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.widgets.backup_list_widget import BackupListWidget
from lib.ui.widgets.buttons.cancel_button import CancelButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.buttons.revert_button import RevertButton


class _BackupDialogButtonsLayout(QHBoxLayout):
    """
    Layout for Backup Dialog Buttons field
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.revert_button = RevertButton()
        self.remove_button = RemoveButton()
        self.cancel_button = CancelButton()
        self.addWidget(self.revert_button)
        self.addWidget(self.remove_button)
        self.addWidget(self.cancel_button)


class BackupDialogLayout(QVBoxLayout):
    """
    Layout for backup dialog
    """
    def __init__(self, backup_manager: BackupManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.BACKUP_DIALOG_LAYOUT)
        self.backup_list = BackupListWidget(backup_manager)
        self.buttons = _BackupDialogButtonsLayout()
        self.addWidget(self.backup_list)
        self.addLayout(self.buttons)
