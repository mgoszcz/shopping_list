"""
Module with all events implementation
"""
from threading import Event

AUTO_SAVE_PAUSED = Event()


class SaveNeededEvent(Event):
    """
    Implementation of save needed class - used by auto save mechanism,
    if auto save is paused then this event will be not set
    """
    def set(self):
        if not AUTO_SAVE_PAUSED.is_set():
            super().set()
        else:
            print('Auto Save paused')


SAVE_NEEDED = SaveNeededEvent()
