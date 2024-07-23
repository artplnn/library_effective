import json


class DatabaseLibrary:
    @staticmethod
    def create_db():
        return open('library_db.txt', 'a+').close()

    @staticmethod
    def connect_to_db(mode):
        return open('library_db.txt', mode)

    @staticmethod
    def read_db():
        with DatabaseLibrary.connect_to_db("r") as file:
            return file.readlines()

    @staticmethod
    def auto_id() -> int:
        lines = DatabaseLibrary.read_db()
        if lines:
            return json.loads(lines[-1])["id"] + 1
        else:
            return 1
