"""
Module contains classes _CategoryButtonsLayout, _CategoryListLayout, _AddCategoryLayout and CategoriesDialogLayout
"""
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout  # pylint: disable=no-name-in-module

from lib.save_load.events import SAVE_NEEDED
from lib.shop.shops_list import ShopsList
from lib.shopping_categories.category_list import CategoryList
from lib.ui.object_names.object_names import ObjectNames
from lib.ui.signals.list_signals import LIST_SIGNALS
from lib.ui.widgets.buttons.add_button import AddButton
from lib.ui.widgets.buttons.move_buttons import MoveUpButton, MoveDownButton, MoveToTopButton, MoveToBottomButton
from lib.ui.widgets.buttons.remove_button import RemoveButton
from lib.ui.widgets.category_list_widget import CategoryListWidget
from lib.ui.widgets.combo_boxes.category_combo_box import CategoryComboBox


class _CategoryButtonsLayout(QVBoxLayout):
    """
    Implements category dialog buttons field
    """
    def __init__(self):
        super().__init__()
        self.move_up_button = MoveUpButton()
        self.move_down_button = MoveDownButton()
        self.remove_button = RemoveButton()
        self.move_top_button = MoveToTopButton()
        self.move_bottom_button = MoveToBottomButton()
        self.addWidget(self.move_top_button)
        self.addWidget(self.move_up_button)
        self.addWidget(self.move_down_button)
        self.addWidget(self.move_bottom_button)
        self.addWidget(self.remove_button)


class _CategoryListLayout(QHBoxLayout):
    """
    Implements category list layout
    """
    def __init__(self, category_list: CategoryList):
        super().__init__()
        self._category_list = category_list
        self.category_list_widget = CategoryListWidget(self._category_list)
        self.buttons = _CategoryButtonsLayout()
        self.addWidget(self.category_list_widget)
        self.addLayout(self.buttons)

        self._disable_up_down_buttons_when_needed()

        self.category_list_widget.itemSelectionChanged.connect(self._disable_up_down_buttons_when_needed)
        self.buttons.remove_button.pressed.connect(self._remove_category)
        self.buttons.move_up_button.pressed.connect(self._move_up_category)
        self.buttons.move_down_button.pressed.connect(self._move_down_category)
        self.buttons.move_top_button.pressed.connect(self._move_top_category)
        self.buttons.move_bottom_button.pressed.connect(self._move_bottom_category)

    def _disable_up_down_buttons_when_needed(self):
        """
        Disable moving buttons when needed
        """
        self.buttons.move_up_button.setDisabled(False)
        self.buttons.move_down_button.setDisabled(False)
        self.buttons.move_bottom_button.setDisabled(False)
        self.buttons.move_top_button.setDisabled(False)
        items_count = self.category_list_widget.count()
        selected_qmodel_index_list = self.category_list_widget.selectedIndexes()
        if not selected_qmodel_index_list:
            self.buttons.move_up_button.setDisabled(True)
            self.buttons.move_down_button.setDisabled(True)
            self.buttons.move_bottom_button.setDisabled(True)
            self.buttons.move_top_button.setDisabled(True)
            return
        index = selected_qmodel_index_list[0].row()
        if items_count == 1:
            self.buttons.move_up_button.setDisabled(True)
            self.buttons.move_down_button.setDisabled(True)
            self.buttons.move_bottom_button.setDisabled(True)
            self.buttons.move_top_button.setDisabled(True)
        elif index == 0:
            self.buttons.move_up_button.setDisabled(True)
            self.buttons.move_top_button.setDisabled(True)
        elif index + 1 == items_count:
            self.buttons.move_down_button.setDisabled(True)
            self.buttons.move_bottom_button.setDisabled(True)
        else:
            pass

    def _move_up_category(self):
        category = self.category_list_widget.currentItem().text()
        row = self.category_list_widget.currentRow()
        self._category_list.move_up(category)
        self.category_list_widget.setCurrentRow(row - 1)

    def _move_down_category(self):
        category = self.category_list_widget.currentItem().text()
        row = self.category_list_widget.currentRow()
        self._category_list.move_down(category)
        self.category_list_widget.setCurrentRow(row + 1)

    def _move_top_category(self):
        category = self.category_list_widget.currentItem().text()
        self._category_list.move_top(category)
        self.category_list_widget.setCurrentRow(0)

    def _move_bottom_category(self):
        category = self.category_list_widget.currentItem().text()
        self._category_list.move_bottom(category)
        self.category_list_widget.setCurrentRow(self.category_list_widget.count() - 1)

    def _remove_category(self):
        selected_item = self.category_list_widget.currentItem()
        if selected_item:
            self._category_list.remove(selected_item.text())


class _AddCategoryLayout(QHBoxLayout):
    """
    Implements add category field layout
    """
    def __init__(self, category_list: CategoryList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._category_list = category_list
        self.category_combobox = CategoryComboBox(self._category_list)
        self.add_button = AddButton()
        self.addWidget(self.category_combobox)
        self.addWidget(self.add_button)


class CategoriesDialogLayout(QVBoxLayout):
    """
    Implements categories dialog layout
    """
    def __init__(self, shops_list: ShopsList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(ObjectNames.CATEGORIES_DIALOG_LAYOUT)
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
        """
        Action when add category button is pressed - add category to shop
        """
        selected_to_add = self.combobox_layout.category_combobox.currentText()
        selected_on_list = self.category_list_layout.category_list_widget.currentIndex().row()
        if selected_to_add in self._shops_list.selected_shop.category_list:
            raise RuntimeError(f'Category {selected_to_add} already in shop')
        self._shops_list.selected_shop.category_list.insert(selected_on_list + 1, selected_to_add)
        SAVE_NEEDED.set()
        LIST_SIGNALS.category_list_changed.emit()

    def disable_add_button_when_item_added(self):
        """
        Disable button if selected category is already on the list
        """
        selected = self.combobox_layout.category_combobox.currentText()
        if selected in self._shops_list.selected_shop.category_list:
            self.combobox_layout.add_button.setDisabled(True)
        else:
            self.combobox_layout.add_button.setDisabled(False)
