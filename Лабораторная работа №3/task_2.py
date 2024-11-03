def find_common_participants(group1, group2, separator=','):

    participants_group1 = set(group1.split(separator))
    participants_group2 = set(group2.split(separator))


    common_participants = sorted(participants_group1.intersection(participants_group2))

    return common_participants



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)

print(common_participants)


