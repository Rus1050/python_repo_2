import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class WoodenPlank:
    def __init__(self, length: float, width: float, amount: int):
        """
           Создание и подготовка к работе объекта "Доски"

           :param length: Длина доски
           :param width: Ширина доски
           :param amount: Колличество досок

           Примеры:
           >>> planks = WoodenPlank(500, 40, 15)  # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина доски должны быть типа int или float")
        if not isinstance(length, (int, float)):
            raise TypeError("Длина доски должны быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина доски должен быть положительным числом")
        if length <= 0:
            raise ValueError("Длина доски должен быть положительным числом")
        self.length = length
        self.width = width
        if not isinstance(amount, int):
            raise TypeError("Количество досок должно быть типа int")
        if amount < 0:
            raise ValueError("Количество досок не может быть отрицательным числом")
        self.amount = amount

    def cut(self, len1: float, len2: float):
        """
        Функция распиливает доски по длине на 2 части.
        Функция удаляет исходный объект и создаёт 2 новых объекта с измененными атрибутами length

        :param len1: Длина первой части распиленной доски
        :param len2: Длина второй части распиленной доски

        :raise ValueError: Если сумма длин распиленных досок превышает изначальную длинну, то вызывается ошибка

        Примеры:
        >>> planks = WoodenPlank(500, 40, 15)
        >>> planks.cut(200,300)
        """
        if not isinstance(len1, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if not isinstance(len2, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if len1 <= 0:
            raise ValueError("Длина должна быть положительным числом")
        if len2 <= 0:
            raise ValueError("Длина должна быть положительным числом")
        ...

    def remove(self, amount_rem: int) -> None:
        """
        Функция уменьшает количество досок в объекте.

        :param amount_rem: Количество извлеченных досок

        :raise ValueError: Если количество изъятых досок превышает изначальное количество, вызывается ошибка

        Примеры:
        >>> planks = WoodenPlank(500, 40, 15)
        >>> planks.remove(5)
        """
        if not isinstance(amount_rem, int):
            raise TypeError("Количество досок должно быть типа int")
        if amount_rem < 0:
            raise ValueError("Количество досок должно быть неотрицательным числом")

    def add(self, amount_add: int) -> None:
        """
        Функция увеличивает количество досок в объекте.

        :param amount_add: Количество добавленных досок

        Примеры:
        >>> planks = WoodenPlank(500, 40, 15)
        >>> planks.add(5)
        """
        if not isinstance(amount_add, int):
            raise TypeError("Количество досок должно быть типа int")
        if amount_add < 0:
            raise ValueError("Количество досок должно быть неотрицательным числом")


class Account:
    def __init__(self, username: str, age: int, password: str):
        """
        Создание и подготовка к работе объекта "Аккаунт"

        :param username: Имя пользователя
        :param age: Возраст пользователя
        :param password: Пароль пользователя

        Примеры:
        >>> John = Account("John", 40, "John_123")  # инициализация экземпляра класса
        """

        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        self.username = username
        if not isinstance(age, int):
            raise TypeError("Возраст пользователя должен быть типа int")
        if age <= 0:
            raise TypeError("Возраст пользователя должен быть положительным числом")
        self.age = age
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть типа str")
        self.password = password

    def birthday(self) -> None:
        """
        Увеличение возраста пользователя на 1.
        Изменяет атрибут age на + 1.
        Примеры:
        >>> John = Account("John", 40, "John_123")
        >>> John.birthday()
        """
        self.age += 1

    def change_password(self, new_password: str) -> None:
        """
        Изменение пароля пользователя.
        Изменяет атрибут password.
        Примеры:
        >>> John = Account("John", 40, "John_123")
        >>> John.change_password("John_321")
        """
        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть типа str")
        self.password = new_password


class Zoo:
    def __init__(self, species: str, amount: int, food: bool = False):
        """
        Создание и подготовка к работе объекта "Зоопарк"

        :param species: Вид животных
        :param amount: Количетсво животных в вольере
        :param food: Есть ли еда у животных

        Примеры:
        >>> tigers = Zoo("feline" ,5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид животного должен типа str")
        self.species = species
        if not isinstance(amount, int):
            raise TypeError("Количество животных должно быть типа int")
        if amount < 0:
            raise TypeError("Количество животных должно быть неотрицательным числом")
        self.amount = amount
        if not isinstance(food, bool):
            raise TypeError("Наличие еды должно быть типа bool")
        self.food = food

    def are_fed(self) -> bool:
        """
        Функция которая проверяет, накормлены ли животные

        :return: Есть ли еда у животных

        Примеры:
        >>> tigers = Zoo("feline" ,5)
        >>> tigers.are_fed()
        """
        ...

    def feed(self) -> None:
        """
        Кормление животных
        Изменяет атрибут food объекта на True.

        Примеры:
        >>> tigers = Zoo("feline" ,5)
        >>> tigers.feed()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
