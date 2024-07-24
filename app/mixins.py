class InputMixin:
    @staticmethod
    def input(prompt: str) -> str:
        """
        Метод для ввода пользовательского ввода
        :param prompt: Строка для вывода в консоль
        :return: Введенная пользователем строка, очищенный от пробелов
        """
        return input(prompt).strip()
