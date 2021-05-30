"""Module contains ServerBackup class"""
import json


class ServerBackup:
    """Implementation of server backup mechanism"""
    def __init__(self, server_dictionary: dict, backup_name: str = 'backup'):
        self.server_dictionary = server_dictionary
        self._backup_name = backup_name

    def create_backup(self):
        """Create backup of current data on server"""
        with open(f'{self._backup_name}.json', 'w') as file:
            json.dump(self.server_dictionary, file)

    def load_backup(self) -> dict:
        """Load data from backup file"""
        with open(f'{self._backup_name}.json') as file:
            data = json.load(file)
        return data
