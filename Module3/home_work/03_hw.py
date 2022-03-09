# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
numbers_list = [10, -7, 95, 62, -38]
even_positive_sum = 0
for number in numbers_list:
    if number > 0 and number % 2 == 0:
        even_positive_sum += number
print(even_positive_sum)
