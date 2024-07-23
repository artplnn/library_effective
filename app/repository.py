import json
from app.db import DatabaseLibrary


class Repository:
    @classmethod
    def select_all(cls) -> list:
        books = []
        for book in DatabaseLibrary.read_db():
            book = json.loads(book)
            books.append(book)
        return books

    @classmethod
    def add_book(cls, title: str, author: str, year: int, status="в наличии") -> None:
        DatabaseLibrary.create_db()
        book = {
            "id": DatabaseLibrary.auto_id(),
            "title": title,
            "author": author,
            "year": year,
            "status": status
        }
        with DatabaseLibrary.connect_to_db("a") as file:
            file.write(json.dumps(book) + '\n')
        print("Книга добавлена успешно")

    @classmethod
    def delete_book(cls, id: int) -> None:
        with DatabaseLibrary.connect_to_db("w") as file:
            for book in DatabaseLibrary.read_db():
                book = json.loads(book)
                if book["id"] != id:
                    file.write(json.dumps(book) + '\n')
        print("Книга удалена успешно")

    @classmethod
    def search_book(cls, title: str = None, author: str = None, year: int = None) -> str or list:
        found_books = [
            book for book in Repository.select_all() if book["title"] == title or book["author"] == author or book["year"] == year
        ]
        return f"Найдены следующие книги: {found_books}"

    @classmethod
    def update_status(cls, id: int, new_status: str) -> None:
        with DatabaseLibrary.connect_to_db("w") as file:
            for book in DatabaseLibrary.read_db():
                book = json.loads(book)
                if book["id"] == id:
                    book["status"] = new_status
                    file.write(json.dumps(book) + '\n')
                else:
                    file.write(json.dumps(book) + '\n')
        print("Статус книги успешно обновлен")
