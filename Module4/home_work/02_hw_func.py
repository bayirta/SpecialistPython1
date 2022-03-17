# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
def distance(x1, y1, x2, y2):
       return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

A = (-3, -1)
B = (2, 4)
C = (1, -3)

list_of_dist = [
    {
        'name': 'AB',
        'distance': distance(*A, *B)
    },
    {
        'name': 'BC',
        'distance': distance(*B, *C)
    },
    {
        'name': 'AC',
        'distance': distance(*A, *C)
    }
]

min_segm = list_of_dist[0]
for segment in list_of_dist:
    if segment['distance'] < min_segm['distance']:
        min_segm = segment

print("Самый короткий отрезок:", min_segm['name'])  # Выводим название отрезка, например “АС”.
