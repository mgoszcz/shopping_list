"""Module contains AddArticleTextEntry class"""
from PyQt5 import QtGui  # pylint: disable=no-name-in-module
from PyQt5.QtCore import Qt  # pylint: disable=no-name-in-module
from PyQt5.QtGui import QFocusEvent  # pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QLineEdit  # pylint: disable=no-name-in-module

from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.add_article_combo_signals import ADD_ARTICLE_COMBO_SIGNALS


class AddArticleTextEntry(QLineEdit):
    """add article text entry implementation, add article text entry is part of add article combo box"""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.ADD_ARTICLE_TEXT_ENTRY)
        ADD_ARTICLE_COMBO_SIGNALS.list_view_key_pressed.connect(self.setFocus)

    def focusInEvent(self, event: QFocusEvent) -> None:  # pylint: disable=invalid-name
        """Overload method to have specific signal emitted"""
        super().focusInEvent(event)
        ADD_ARTICLE_COMBO_SIGNALS.text_edit_focus_in.emit()

    def focusOutEvent(self, event: QFocusEvent) -> None:  # pylint: disable=invalid-name
        """Overload method to have specific signal emitted"""
        super().focusOutEvent(event)
        ADD_ARTICLE_COMBO_SIGNALS.text_edit_focus_out.emit()

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:  # pylint: disable=invalid-name
        """Overload method to have specific signal emitted"""
        super().keyReleaseEvent(a0)
        if a0.key() == Qt.Key_Down:
            ADD_ARTICLE_COMBO_SIGNALS.text_edit_key_down.emit()
