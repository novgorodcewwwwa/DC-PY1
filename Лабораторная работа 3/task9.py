salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

while True:
    need_money += - (salary - spend)
    spend *= 1.00 + increase
    months -= 1
    if months == 0:
        break


print(round(need_money))
