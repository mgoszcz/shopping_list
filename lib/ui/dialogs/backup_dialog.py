from PyQt5.QtWidgets import QDialog

from lib.backup_manager.backup_manager import BackupManager
from lib.ui.dialogs.confirm_dialog import ConfirmDialog
from lib.ui.layouts.backup_dialog_layout import BackupDialogLayout
from lib.ui.signals.list_signals import LIST_SIGNALS


class BackupDialog(QDialog):

    def __init__(self, backup_manager: BackupManager):
        super().__init__()
        self._backup_manager = backup_manager
        self.layout = BackupDialogLayout(self._backup_manager)
        self.setLayout(self.layout)

        self.layout.buttons.revert_button.pressed.connect(self.revert_backup)
        self.layout.buttons.cancel_button.pressed.connect(self.reject)
        self.layout.buttons.remove_button.pressed.connect(self.remove_backup)

    def revert_backup(self):
        backup_name = self.layout.backup_list.currentItem().text()
        print(f'aaa {backup_name}')
        LIST_SIGNALS.blockSignals(True)
        self._backup_manager.restore_backup(backup_name)
        LIST_SIGNALS.blockSignals(False)
        self.accept()

    def remove_backup(self):
        backup_name = self.layout.backup_list.currentItem().text()
        if ConfirmDialog(f'Czy na pewno chcesz usunąć backup {backup_name}?').exec_():
            self._backup_manager.remove_backup(backup_name)
            self.layout.backup_list.populate_list()