"""Module with FileObject class"""
import os


class FileObjectException(BaseException):
    """Custom exception for file operations errors"""
    pass


class FileObject:
    """Class represents file it can return path to ir and do some actions on file"""
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        self._file_path = file_path

    def exists(self) -> bool:
        return os.path.exists(self._file_path)

    def remove(self) -> None:
        """Remove file, in case of exception raise one unique exception FileObjectException"""
        try:
            os.remove(self._file_path)
        except FileNotFoundError:
            raise FileObjectException(f'File {self._file_path} not found')
        except PermissionError:
            raise FileObjectException(f'Access to file {self._file_path} denied')
