from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout  # pylint: disable=no-name-in-module

from lib.backup_manager.backup_manager import BackupManager
from lib.ui.widgets.backup_list_widget import BackupListWidget
from lib.ui.widgets.buttons.cancel_button import CancelButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.buttons.revert_button import RevertButton


class _BackupDialogButtonsLayout(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.revert_button = RevertButton()
        self.remove_button = RemoveButton()
        self.cancel_button = CancelButton()
        self.addWidget(self.revert_button)
        self.addWidget(self.remove_button)
        self.addWidget(self.cancel_button)


class BackupDialogLayout(QVBoxLayout):

    def __init__(self, backup_manager: BackupManager):
        super().__init__()
        self.backup_list = BackupListWidget(backup_manager)
        self.buttons = _BackupDialogButtonsLayout()
        self.addWidget(self.backup_list)
        self.addLayout(self.buttons)




