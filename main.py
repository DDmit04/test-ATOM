#coding=utf-8
from __future__ import print_function

from collections import deque

"""
Постановка:

На бесконечной координатной сетке находится муравей. Муравей может перемещаться на 1 клетку
вверх (x,y+1), вниз (x,y-1), влево (x-1,y), вправо (x+1,y), по одной клетке за шаг.

Клетки, в которых сумма цифр в координате X плюс сумма цифр в координате Y больше чем 25 недоступны муравью.
Например, клетка с координатами (59, 79) недоступна, т.к. 5+9+7+9=30, что больше 25.

Сколько клеток может посетить муравей, если его начальная позиция (1000,1000), (включая начальную клетку)

-----------------------------------------------------------------------------------------------------------------------

Логика решения: 

Обычный обход в ширину из данной клетки, который происходит за O(n), где n - количество точек в результате
"""
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def digit_sum(num):
    return sum(map(int, str(abs(num))))

def is_cell_allowed(_x, _y, _cap):
    return digit_sum(_x) + digit_sum(_y) <= _cap

def calc_ant_cells(start_x, start_y, _cap):

    if not is_cell_allowed(_x, _y, _cap) or _cap <= 0:
        return 0
    
    start = (start_x, start_y)

    q = deque([start])
    visited = set([start])

    while q:
        _x, _y = q.popleft()

        for dx, dy in MOVES:
            new_x = _x + dx
            new_y = _y + dy

            in_visited = (new_x, new_y) not in visited
            if not in_visited:
                continue
            
            is_allowed = is_cell_allowed(new_x, new_y, _cap)
            if not is_allowed:
                continue
                
            visited.add((new_x, new_y))
            q.append((new_x, new_y))

    return len(visited)


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
    print(u"Доступных клеток:", calc_ant_cells(x, y, cap))
