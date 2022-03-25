# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.
while True:
    raw_data = input("Введите 5 целых чисел через пробел ")
    try:
        list_of_el = raw_data.split()
        list_of_int = []
        for el in list_of_el:
            if len(list_of_el) == 5:
                list_of_int.append(int(el))
            else:
                raise ValueError
        break
    except ValueError:
        print("Некорректные данные")
list_of_pos_int = []
for int_el in list_of_int:
    if int_el > 0:
        list_of_pos_int.append(int_el)
# print(list_of_pos_int)
try:
    list_of_pos_int != []
    min_int = list_of_pos_int[0]
    for int_pos_el in list_of_pos_int:
        if int_pos_el < min_int:
            min_int = int_pos_el
    print(min_int)
except:
    print("Положительных чисел нет")
