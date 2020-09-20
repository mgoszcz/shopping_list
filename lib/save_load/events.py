from threading import Event

AUTO_SAVE_PAUSED = Event()


class SaveNeededEvent(Event):

    def set(self):
        if not AUTO_SAVE_PAUSED.is_set():
            super(SaveNeededEvent, self).set()
        else:
            print('Auto Save paused')


SAVE_NEEDED = SaveNeededEvent()
