money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = salary - spend
while (money_capital + delta) >= spend:
    money_capital = money_capital + delta
    month = month + 1
    spend = spend * (1.00 + increase)

print(month)

# month = 0  # количество месяцев, которое можно прожить
#
# while (money_capital + salary - spend) >= spend:
#     money_capital = money_capital + salary - spend
#     month = month + 1
#     spend = spend * (1.00 + increase)
#
# print(month)
