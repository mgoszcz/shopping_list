from PyQt5.QtWidgets import QHBoxLayout

from lib.backup_manager.backup_manager import BackupManager
from lib.ui.dialogs.backup_dialog import BackupDialog
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.buttons.backup_button import BackupButton


class BackupLayout(QHBoxLayout):

    def __init__(self, backup_manager: BackupManager):
        super().__init__()
        self.backup_button = BackupButton()

        self._backup_dialog = BackupDialog(backup_manager)

        self.addWidget(self.backup_button)

        self.backup_button.pressed.connect(self.backup)

    def backup(self):
        self._backup_dialog.layout.backup_list.populate_list()
        self._backup_dialog.exec_()
        LIST_SIGNALS.emit_all()