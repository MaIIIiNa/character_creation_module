from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выдате ответ."""
    if your_number <= 0:
        return

    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {CalculateSquareRoot(your_number)}')


print(message)
calc(25.5)
