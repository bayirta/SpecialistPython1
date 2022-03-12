# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here


# Не забудьте протестировать вашу функцию

def distance(x1, y1, x2, y2):
    # TODO: your code here
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def triangle(p1, p2, p3):
    # TODO: your code here

    a = distance(*p1, *p2)
    b = distance(*p1, *p3)
    c = distance(*p3, *p2)

    if a < b + c and b < a + c and c < b + a:
        p = a + b + c
        S = (p*(p-a)*(p-b)*(p-c))**0.5
        return p, S
    return "impossible"
# Пример вызова функции
print(triangle((10, 10), (14, 14), (12, 12)))
