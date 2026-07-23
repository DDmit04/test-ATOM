#coding=utf-8
from __future__ import print_function

class BackwardNumSumIterator(object):
    def __init__(self, start):
        self.current = start
        self.sum = get_dij_sum(start)
        self.direction = -1

    def next(self):
        if self.current % 10 != 0:
            self.sum += self.direction
        else:
            self.sum = get_dij_sum(self.current + self.direction)

        self.current += self.direction
        return self.sum

    def __iter__(self):
        return self


def get_dij_sum(dijit):
    return sum(map(int, str(dijit)))


def get_square(diameter):
    return (diameter + 1) ** 2 + diameter ** 2


def calc_ant_cells(x, y, cap):
    x = abs(x)
    y = abs(y)
    x += y

    if get_dij_sum(x) > cap or cap <= 0:
        return 0

    full_diameter = x + (cap - get_dij_sum(x))
    full_square = get_square(full_diameter)

    d_sum = BackwardNumSumIterator(x)

    # +1 потому что в конце будет лишняя итерация
    while d_sum.sum <= cap + 1 and d_sum.current > 0:
        d_sum.next()

    if d_sum.current == 0:
        border_square = 0
    else:
        border_diameter = d_sum.current
        border_square = get_square(border_diameter)

    print(u"Радиус внешнего ромба:", full_diameter)
    print(u"Площадь внешнего ромба: ", full_square)
    print(u"Радиус внутреннего ромба: ", d_sum.sum)
    print(u"Площадь внутреннего ромба: ", border_square)

    return full_square - border_square


def input_positive_int(msg):
    res = None
    while res is None:
        try:
            res = int(raw_input(msg))
            if res < 0:
                raise ValueError
        except ValueError:
            print(u"Неверный ввод")

    return res or 0

if __name__ == '__main__':
    x = input_positive_int("координата X: ")
    y = input_positive_int("координата Y: ")
    cap = input_positive_int("Сумма: ")

    print("Доступных клеток:", calc_ant_cells(x, y, cap))
