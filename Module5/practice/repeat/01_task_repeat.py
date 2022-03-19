# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of, to):
    my_list = []
    for _ in range (size):
        my_list.append(random.randint(of, to))
    return my_list

print(gen_list(5, 2, 99))

