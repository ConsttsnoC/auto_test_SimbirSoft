from datetime import datetime


def fibonacci(n: int) -> int:
    """
    Вычисляет N-е число Фибоначчи.

    :param n: Позиция в последовательности Фибоначчи.
    :return: N-е число Фибоначчи.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def get_fibonacci_for_today() -> int:
    """
    Вычисляет число Фибоначчи для текущего дня месяца + 1.

    :return: Число Фибоначчи для текущего дня месяца + 1.
    """
    today = datetime.now()
    day_of_month = today.day
    n = day_of_month + 1
    return fibonacci(n)
