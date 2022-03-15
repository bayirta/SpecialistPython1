# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    first_three = int(str(ticket_number)[:3])
    last_three = int(str(ticket_number)[3:])
    s1 = first_three // 100 + first_three % 100 // 10 + first_three % 10
    s2 = last_three // 100 + last_three % 100 // 10 + last_three % 10
    return s1 == s2

print(lucky_ticket(300111)) #не позволяет проверить, если первая цифра нуль

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
