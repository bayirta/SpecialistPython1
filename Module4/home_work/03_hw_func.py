# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def circle_in_circle(center1, center2, R1, R2):
   return distance(*center1, *center2) < abs(R2 - R1)

print(circle_in_circle((-2, 1), (-1.75, 1), 2, 1.75))
print(circle_in_circle((-2, 1), (-1.5, 1), 2, 1))
print(circle_in_circle((-2, 1), (2, 1), 2, 2))
print(circle_in_circle((-2, 1), (1, 2), 2, 2))
