# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

# TODO: your code here

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
# i = 1
# width = len(max(fruits, key = len))
# for fruit in fruits:
#     fruit = fruit.rjust(width, ' ')
#     print(str(i) + ". " + fruit)
#     i += 1

longest_fruit = []
for fruit in fruits:
    if len(fruit) > len(longest_fruit):
        longest_fruit = fruit
i = 1
width = len(longest_fruit)
for fruit in fruits:
    fruit = fruit.rjust(width, ' ')
    print(str(i) + ". " + fruit)
    i += 1
