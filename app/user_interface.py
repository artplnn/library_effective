from app.mixins import InputMixin
from app.repository import Repository


class UserInterface(InputMixin):

    def process(self):
        """
        Основной цикл интерфейса приложения
        """
        while True:
            try:
                print(
                "\n",
                "Выберите действие:",
                "1. Добавить книгу",
                "2. Удалить книгу",
                "3. Поиск книги",
                "4. Показать все книги",
                "5. Обновить статус книги",
                "6. Выйти",
                sep="\n",
                )

                action = self.input("Введите номер действия: ")

                match action:

                    case "1":
                        title = self.input("Введите название книги: ")
                        author = self.input("Введите автора книги: ")
                        year = int(self.input("Введите год издания книги: "))
                        Repository.add_book(title, author, year)

                    case "2":
                        id_ = int(self.input("Введите ID книги для удаления: "))
                        Repository.delete_book(id_)

                    case "3":
                        print(
                            "Выберите поиск по:",
                            "1. Названию",
                            "2. Автору",
                            "3. Году издания",
                            sep="\n",
                            )

                        search_type = self.input("Введите номер поиска: ")
                        match search_type:
                            case "1":
                                input_title = self.input("Введите название книги для поиска: ")
                                print(Repository.search_book(title=input_title))
                            case "2":
                                input_author = self.input("Введите автора книги для поиска: ")
                                print(Repository.search_book(author=input_author))
                            case "3":
                                input_year = int(self.input("Введите год издания книги для поиска: "))
                                print(Repository.search_book(year=input_year))
                            case _:
                                print("Ошибка: введен неверный номер поиска.")

                    case "4":
                        print(Repository.select_all())

                    case "5":
                        id_ = int(self.input("Введите ID книги для изменения статуса: "))
                        new_status = self.input("Введите новый статус книги (в наличии/выдана): ")
                        if new_status.lower() in ["в наличии", "выдана"]:
                            Repository.update_status(id_, new_status)
                        else:
                            print("Ошибка: введен неверный статус книги. Допустимый статусы: в наличии/выдана.")

                    case "6":
                        break

                    case _:
                        print("Ошибка: введен неверный номер действия.",
                              "Пожалуйста, введите команду от 1 до 6.")

            except Exception:
                print("Ошибка: неверный формат ввода.")