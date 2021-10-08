"""
Module contains  BackupDialog class
"""
from PyQt5.QtWidgets import QDialog  # pylint: disable=no-name-in-module

from lib.backup_manager.backup_manager import BackupManager
from lib.ui.dialogs.confirm_dialog import ConfirmDialog
from lib.ui.icons.icons import ShoppingListIcon
from lib.ui.layouts.backup_dialog_layout import BackupDialogLayout
from lib.ui.signals.list_signals import LIST_SIGNALS


class BackupDialog(QDialog):
    """
    Implementation of Backup Dialog
    """
    def __init__(self, backup_manager: BackupManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._backup_manager = backup_manager
        self.setWindowTitle('Punkty przywracania')
        self.setWindowIcon(ShoppingListIcon.q_icon())
        self.layout = BackupDialogLayout(self._backup_manager)
        self.setLayout(self.layout)

        self.layout.buttons.revert_button.pressed.connect(self.revert_backup)
        self.layout.buttons.cancel_button.pressed.connect(self.reject)
        self.layout.buttons.remove_button.pressed.connect(self.remove_backup)

    def revert_backup(self):
        """
        Action when pressing revert button - reverts database from specific backup file
        """
        backup_name = self.layout.backup_list.currentItem().text()
        LIST_SIGNALS.blockSignals(True)
        self._backup_manager.restore_backup(backup_name)
        LIST_SIGNALS.blockSignals(False)
        self.accept()

    def remove_backup(self):
        """
        Action when pressing remove backup - removes backup file
        """
        backup_name = self.layout.backup_list.currentItem().text()
        if ConfirmDialog(f'Czy na pewno chcesz usunąć backup {backup_name}?').exec_():
            self._backup_manager.remove_backup(backup_name)
            self.layout.backup_list.populate_list()
