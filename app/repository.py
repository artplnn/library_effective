import json

from app.config import ConfigModeOpenFile, BookCase
from app.db import Database


class Repository:
    @classmethod
    def select_all(cls) -> list:
        """
        Возвращает список всех книг из файла (базы данных)
        """
        books = []
        for book in Database.read_db():
            book = json.loads(book)
            books.append(book)
        return books

    @classmethod
    def add_book(cls, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в файл (базу данных)
        :param id: id книги
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :param status: в наличии (по умолчанию)/выдана
        """
        book = {
            BookCase.ID: Database.auto_id(),
            BookCase.TITLE: title,
            BookCase.AUTHOR: author,
            BookCase.YEAR: year,
            BookCase.STATUS: "в наличии"
        }
        Database.add_to_db(book)
        print("Книга добавлена успешно")

    @classmethod
    def delete_book(cls, id_: int) -> None:
        """
        Удаляет книгу из файла (базы данных) по ID
        :param id_: ID книги
        """
        lines = Database.read_db()
        with Database.connect_to_db(ConfigModeOpenFile.READ) as file:
            for i, book in enumerate(lines):
                book = json.loads(book)
                if book[BookCase.ID] == id_:
                    del lines[i]
                    file.seek(0)
                    file.truncate()
                    file.writelines(lines)
                    print("Книга удалена успешно")
                    return
            print("Книга не найдена")

    @classmethod
    def search_book(cls, title: str = None, author: str = None, year: int = None) -> str:
        """
        Поиск книг по одному из заданных параметров
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :return: Строка с найденными книгами
        """
        found_books = [
            book for book in Repository.select_all()
            if book[BookCase.TITLE] == title or book[BookCase.AUTHOR] == author or book[BookCase.YEAR] == year
        ]

        return f"Найдены следующие книги: {found_books}"

    @classmethod
    def update_status(cls, id_: int, new_status: str) -> None:
        """
        Изменяет статус книги в файле (базе данных) по ID
        :param id_: ID книги
        :param new_status: Новый статус книги (в наличии/выдана)
        """
        lines = Database.read_db()
        with Database.connect_to_db(ConfigModeOpenFile.WRITE) as file:
            for book in lines:
                book = json.loads(book)
                if book[BookCase.ID] == id_:
                    book[BookCase.STATUS] = new_status
                    print("Статус книги изменен успешно")
                file.write(json.dumps(book, ensure_ascii=False) + '\n')
