from PyQt5.QtCore import QObject


def get_parent_object(child_object: QObject, parent_name: str) -> QObject:
    parent = child_object.parentWidget()
    while not parent.objectName() == parent_name:
        parent = parent.parentWidget()
    return parent
