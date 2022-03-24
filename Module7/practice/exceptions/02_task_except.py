# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
def high_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

while True:
    month_year = input("Введите месяц и год в формате mm yyyy ")
    try:
        month = int(month_year.split(" ")[0])
        year = int(month_year.split(" ")[1])
        if month > 12 or month <= 0 or year < 0:
            raise ValueError
        break
    except (ValueError, IndexError):
        print("Неверный формат")

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
   print(f"В {month} месяце {year} года 31 день")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"В {month} месяце {year} года 30 дней")
elif high_year(year):
    print(f"В {month} месяце {year} года 29 дней")
else:
    print(f"В {month} месяце {year} года 28 дней")
