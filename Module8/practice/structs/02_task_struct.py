# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
numbers = [1, 2, 4, 5, 6, 2, 5, 2]

unique_numbers = []
non_repeat_numbers = []
for number in numbers:
    if number in unique_numbers:
        pass
    else:
        unique_numbers.append(number)
    if numbers.count(number) == 1:
        non_repeat_numbers.append(number)
print(unique_numbers)
print(non_repeat_numbers)
