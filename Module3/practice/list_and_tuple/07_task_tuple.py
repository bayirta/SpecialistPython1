# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
new_list = list(tup)
max_value = int()
for el in new_list:
    if el > max_value:
        max_value = el
print(max_value)
