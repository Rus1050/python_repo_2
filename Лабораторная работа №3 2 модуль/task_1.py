class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def author(self):
        return self._author  # внутри класса обращаемся к защищенному атрибуту

    @author.setter
    def author(self, new_author : str) -> None:
        self._author = new_author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Объём {self.pages} страниц."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, int):
            raise TypeError("Длительность книги должна быть типа int")
        if duration <= 0:
            raise ValueError("Длительность книги должна быть положительным числом")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration} секунд."


pbook = PaperBook("Prestuplenie and nakazanie", "Dostaevski", 123)
print(pbook)
abook = AudioBook("Master and Margarita", "Bulgakov", 321)
print(abook)