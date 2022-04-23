#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import math

"""
С использованием многопоточности для заданного значения найти сумму ряда с точностью члена ряда по абсолютному
значению 1e-07 и произвести сравнение полученной суммы с контрольным значением функции для двух бесконечных
рядов.
"""

CONST_ABSOLUTE = 1e-07


# Находим контрольное значение
def control_x(x=1):
    return math.pow(3, x)


def control_y(x=-0.8):
    return 5 - 2 * x / (6 - 5 * x + math.pow(x, 2))


def summ_1():
    x = 1
    previous = 0
    s = 0
    n = 0
    curr = (math.pow(x, n) * math.pow(math.log(3), n)) / math.factorial(n)
    s += curr
    n += 1
    while abs(curr - previous) > CONST_ABSOLUTE:
        previous = curr
        curr = (math.pow(x, n) * math.pow(math.log(3), n)) / math.factorial(n)
        n += 1
        s += curr
    return s


def summ_2():
    x = -0.8
    previous = 0
    s = 0
    n = 0
    curr = (1 / math.pow(2, n) + 1 / math.pow(3, n)) * math.pow(x, n-1)
    s += curr
    n += 1
    while abs(curr - previous) > CONST_ABSOLUTE:
        previous = curr
        curr = (1 / math.pow(2, n) + 1 / math.pow(3, n)) * math.pow(x, n-1)
        n += 1
        s += curr
    return s


def compare(x, y):
    result = x - y
    print(f"Результат сравнения {result}")


if __name__ == '__main__':
    th1 = Thread(target=compare(summ_1(), control_x()))
    th1.start()
    th2 = Thread(target=compare(summ_2(), control_y()))
    th2.start()
    th1.join()
    th2.join()
