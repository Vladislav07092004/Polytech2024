def find_common_participants(group1, group2, separator='|'):
    # Разбиваем строки на множества, убираем пробелы вокруг имен
    participants_group1 = {name.strip() for name in group1.split(separator) if name.strip()}
    participants_group2 = {name.strip() for name in group2.split(separator) if name.strip()}

    # Ищем пересечение
    common_participants = participants_group1.intersection(participants_group2)

    return common_participants

# Пример использования
participants_first_group = "Иванов| Петров|Сидоров "
participants_second_group = "Петров|Сидоров| Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)







