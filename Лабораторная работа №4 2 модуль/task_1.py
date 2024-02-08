import doctest
import math


class GeometricShape:
    """ Базовый класс геометрические фигуры. """
    def __init__(self, area: float, perimeter: float):
        """
        Создание и подготовка к работе объекта "Геометрическая фигура"

        :param area: Площадь фигуры
        :param perimeter: Периметр фигуры

        Примеры:
        >>> shape = GeometricShape(1.0, 2.0)  # инициализация экземпляра класса
        """
        self.area = area
        self.perimeter = perimeter

    def __str__(self):
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр и
        предназначенную для чтения человеком.

        Примеры:
        >>> shape = GeometricShape(1.0, 2.0)
        >>> shape.__str__()
        """
        return f"Фигура с площадью {self.area} м² и периметром {self.perimeter} м"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр и
        предназначен для машинно-ориентированного вывода.

        Примеры:
        >>> shape = GeometricShape(1.0, 2.0)
        >>> shape.__repr__()
        """
        return f"{self.__class__.__name__}(area={self.area!r}, perimeter={self.perimeter!r})"

    def draw(self):
        """
        Создает изображение геометрической фигуры
        Метод наследуется в дочерних классах

        Примеры:
        >>> shape = GeometricShape(1.0, 2.0)
        >>> shape.draw()
        """
        ...

    def __eq__(self: 'GeometricShape', other: 'GeometricShape'):

        """
        Метод проверяет, равны ли фигуры,
        сравнивая их площадь и периметр

        :param other: Другой объект класса геометрическая фигура

        Примеры:
        >>> shape = GeometricShape(1.0, 2.0)
        >>> shape2 = GeometricShape(2.0, 1.0)
        >>> shape.__eq__(shape2)
        """
        return self.area == other.area and self.perimeter == other.perimeter


class Circle(GeometricShape):
    """ Дочерний класс круги к базовому классу геометрических фигур. """
    def __init__(self, radius: float, area: float = None, perimeter: float = None):
        """
        Создание и подготовка к работе объекта "круг"

        :param area: Площадь круга
        :param perimeter: Периметр круга
        :param radius: Радиус круга

        Примеры:
        >>> circle = Circle(3.0)  # инициализация экземпляра класса
        """
        super().__init__(area, perimeter)
        if not isinstance(radius, float):
            raise TypeError("Радиус круга должен быть типа float")
        if radius <= 0:
            raise ValueError("Радиус круга должен быть положительным числом")
        self.radius = radius
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    def __str__(self):
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр и
        предназначенную для чтения человеком.
        Перегрузка метода необходима для добавления информации в вывод.

        Примеры:
        >>> circle = Circle(3.0)
        >>> circle.__str__()
        """
        return f"Круг радиусом {self.radius} м, с площадью {self.area} м² и периметром {self.perimeter} м"

    def calculate_area(self):
        """
        Метод пересчитывает значение площади, используя радиус круга
        Метод вызывается при инициализации объекта класса

        Примеры:
        >>> circle = Circle(3.0)
        """
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        """
        Метод пересчитывает значение периметра, используя радиус круга.
        Метод вызывается при инициализации объекта класса

        Примеры:
        >>> circle = Circle(3.0)
        """
        return 2 * math.pi * self.radius

    def __eq__(self: 'Circle', other: 'Circle'):
        """
        Метод проверяет, равны ли круги, сравнивая их радиусы
        Перегрузка метода необходима для упрощения метода

        :param other: Другой объект класса круг

        Примеры:
        >>> circle = Circle(3.0)
        >>> circle2 = Circle(4.0)
        >>> circle.__eq__(circle2)
        """
        return self.radius == other.radius


class Recktangle(GeometricShape):
    """ Дочерний класс прямоугольники к базовому классу геометрических фигур. """
    def __init__(self, height: float, width: float, area: float = None, perimeter: float = None):
        """
        Создание и подготовка к работе объекта "прямоугольник"

        :param area: Площадь прямоугольника
        :param perimeter: Периметр прямоугольника
        :param height: Высота прямоугольника
        :param width: Ширина прямоугольника

        Примеры:
        >>> square = Recktangle(3.0, 3.0)  # инициализация экземпляра класса
        """
        super().__init__(area, perimeter)
        if not isinstance(height, float) and not isinstance(width, float):
            raise TypeError("Размеры прямоугольника должны быть типа float")
        if height <= 0 or width <= 0:
            raise ValueError("Размеры прямоугольника должны быть положительным числом")
        self.height = height
        self.width = width
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()

    def __str__(self):
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр и
        предназначенную для чтения человеком.
        Перегрузка метода необходима для добавления информации в вывод.

        Примеры:
        >>> square = Recktangle(3.0, 3.0)
        >>> square.__str__()
        """
        return f"Прямоугольник высотой {self.height} м, шириной {self.width}," \
               f" с площадью {self.area} м² и периметром {self.perimeter} м"

    def calculate_area(self):
        """
        Метод пересчитывает значение площади, используя размеры прямоугольника
        Метод вызывается при инициализации объекта класса

        Примеры:
        >>> square = Recktangle(3.0, 3.0)
        """
        return self.height * self.width

    def calculate_perimeter(self):
        """
        Метод пересчитывает значение периметра, используя размеры прямоугольника
        Метод вызывается при инициализации объекта класса

        Примеры:
        >>> square = Recktangle(3.0, 3.0)
        """
        return 2 * self.height + self.width * 2

    def __eq__(self: 'Recktangle', other: 'Recktangle'):
        """
        Метод проверяет, равны ли прямоугольники, сравнивая их высоту и ширину
        Перегрузка необходима для упрощения метода

        :param other: Другой объект класса прямоугольник

        Примеры:
        >>> square = Recktangle(3.0, 3.0)
        >>> square2 = Recktangle(4.0, 4.0)
        >>> square.__eq__(square2)
        """
        return self.height == other.height and self.width == other.width


if __name__ == "__main__":
    doctest.testmod()
    pass
