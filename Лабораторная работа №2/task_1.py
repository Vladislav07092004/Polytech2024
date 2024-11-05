money_capital = 20000  # Подушка безопасности
salary = 5000          # Ежемесячная зарплата
spend = 6000           # Траты за первый месяц
increase = 0.05        # Ежемесячный рост цен


months = 0
current_budget = money_capital

# Цикл по месяцам
while current_budget >= spend:
    # Добавляем зарплату к текущему бюджету
    current_budget += salary

    # Вычитаем расходы из бюджета
    current_budget -= spend
    months += 1  # Увеличиваем счётчик месяцев

    # Увеличиваем траты на следующий месяц только начиная со второго месяца
    if months > 1:
        spend *= (1 + increase)


print("Количество месяцев, которое можно протянуть без долгов:", months)


