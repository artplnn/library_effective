import json
from typing import TextIO

from app.config import LIBRARY_DB, ConfigModeOpenFile, BookCase


class Database:

    @staticmethod
    def connect_to_db(mode: str) -> TextIO:
        """
        Метод для коннекта с файлом (базой данных)
        """
        return open(LIBRARY_DB, mode)


    @staticmethod
    def read_db() -> list:
        """
        Метод для чтения файла (базы данных)
        """
        with Database.connect_to_db(ConfigModeOpenFile.READ) as file:
            return file.readlines()

    @staticmethod
    def add_to_db(data) -> None:
        """
        Метод для добавления данных в конец файла
        """
        with Database.connect_to_db(ConfigModeOpenFile.APPEND) as file:
            file.write(json.dumps(data, ensure_ascii=False) + '\n')

    @staticmethod
    def auto_id() -> int:
        """
        Метод для автоинкремента ID
        """
        lines = Database.read_db()
        if lines:
            return json.loads(lines[-1])[BookCase.ID] + 1
        else:
            return 1
