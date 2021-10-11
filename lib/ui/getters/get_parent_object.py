"""Module contains get_parent_object function"""
from PyQt5.QtCore import QObject  # pylint: disable=no-name-in-module


def get_parent_object(child_object: QObject, parent_name: str) -> QObject:
    """Get parent object of specific name in Qt hierarchy"""
    parent = child_object.parentWidget()
    while not parent.objectName() == parent_name:
        parent = parent.parentWidget()
    return parent
