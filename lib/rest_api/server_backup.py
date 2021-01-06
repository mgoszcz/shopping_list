import json


class ServerBackup:

    def __init__(self, server_dictionary: dict):
        self.server_dictionary = server_dictionary

    def create_backup(self):
        with open('backup.json', 'w') as file:
            json.dump(self.server_dictionary, file)

    @staticmethod
    def load_backup() -> dict:
        with open('backup.json') as file:
            data = json.load(file)
        return data
