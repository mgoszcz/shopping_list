"""Module with FileObject class"""
import os


class FileObjectException(BaseException):
    """Custom exception for file operations errors"""


class FileObject:
    """Class represents file it can return path to ir and do some actions on file"""
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    @property
    def file_path(self) -> str:
        """Return path to file represented by this class instance"""
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """Reset path to file represented by this class instance"""
        self._file_path = file_path

    def exists(self) -> bool:
        return os.path.exists(self._file_path)

    def remove(self) -> None:
        """Remove file, in case of exception raise one unique exception FileObjectException"""
        try:
            os.remove(self._file_path)
        except FileNotFoundError as error:
            raise FileObjectException(str(error))
        except PermissionError as error:
            raise FileObjectException(str(error))

    def rename(self, new_name: str) -> None:
        """Rename file, it will remain unchanged path and extension, only new name is needed"""
        file_path, file_name = os.path.split(self._file_path)
        extension = os.path.splitext(file_name)[1]
        try:
            os.rename(self._file_path, os.path.join(file_path, f'{new_name}{extension}'))
            self._file_path = os.path.join(file_path, f'{new_name}{extension}')
        except FileNotFoundError as error:
            raise FileObjectException(str(error))
        except PermissionError as error:
            raise FileObjectException(str(error))
