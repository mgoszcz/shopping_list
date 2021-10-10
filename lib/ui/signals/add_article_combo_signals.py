from PyQt5.QtCore import QObject, pyqtSignal


class AddArticleComboSignals(QObject):
    text_edit_focus_in = pyqtSignal()
    text_edit_focus_out = pyqtSignal()
    list_view_focus_in = pyqtSignal()
    list_view_focus_out = pyqtSignal()
    list_view_key_pressed = pyqtSignal(int)
    list_view_return_pressed = pyqtSignal()
    text_edit_key_down = pyqtSignal()


ADD_ARTICLE_COMBO_SIGNALS = AddArticleComboSignals()
