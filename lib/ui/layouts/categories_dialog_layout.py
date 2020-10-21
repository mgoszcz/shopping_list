from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QListWidget

from lib.shop.shops_list import ShopsList
from lib.shopping_categories.category_list import CategoryList
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.buttons.move_buttons import MoveUpButton, MoveDownButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.category_list_widget import CategoryListWidget
from lib.ui.widgets.combo_boxes.category_combo_box import CategoryComboBox


class _CategoryButtonsLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.move_up_button = MoveUpButton()
        self.move_down_button = MoveDownButton()
        self.remove_button = RemoveButton()
        self.addWidget(self.move_up_button)
        self.addWidget(self.move_down_button)
        self.addWidget(self.remove_button)


class _CategoryListLayout(QHBoxLayout):
    def __init__(self, category_list: CategoryList):
        super().__init__()
        self._category_list = category_list
        self.category_list_widget = CategoryListWidget(self._category_list)
        self.buttons = _CategoryButtonsLayout()
        self.addWidget(self.category_list_widget)
        self.addLayout(self.buttons)


class _AddCategoryLayout(QHBoxLayout):
    def __init__(self, category_list: CategoryList):
        super().__init__()
        self._category_list = category_list
        self.category_combobox = CategoryComboBox(self._category_list)
        self.add_button = AddButton()
        self.addWidget(self.category_combobox)
        self.addWidget(self.add_button)


class CategoriesDialogLayout(QVBoxLayout):
    def __init__(self, shops_list: ShopsList):
        super().__init__()
        self._shops_list = shops_list
        self.combobox_layout = _AddCategoryLayout(self._shops_list.categories)
        self.category_list_layout = _CategoryListLayout(self._shops_list.selected_shop.category_list)
        self.addLayout(self.combobox_layout)
        self.addLayout(self.category_list_layout)

        self.disable_add_button_when_item_added()

        LIST_SIGNALS.category_list_changed.connect(self.disable_add_button_when_item_added)
        self.combobox_layout.category_combobox.activated.connect(self.disable_add_button_when_item_added)
        self.combobox_layout.add_button.pressed.connect(self.add_button_pressed)

    def add_button_pressed(self):
        selected = self.combobox_layout.category_combobox.currentText()
        if selected in self._shops_list.selected_shop.category_list:
            raise RuntimeError(f'Category {selected} already in shop')
        self._shops_list.selected_shop.category_list.append(selected)
        LIST_SIGNALS.category_list_changed.emit()

    def disable_add_button_when_item_added(self):
        selected = self.combobox_layout.category_combobox.currentText()
        if selected in self._shops_list.selected_shop.category_list:
            self.combobox_layout.add_button.setDisabled(True)
        else:
            self.combobox_layout.add_button.setDisabled(False)
