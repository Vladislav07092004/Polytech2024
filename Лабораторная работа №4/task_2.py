# TODO решите задачу
import json


def task() -> float:
    try:
        with open('input.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Ошибка: файл input.json не найден.")
        return 0.0
    except json.JSONDecodeError:
        print("Ошибка: ошибка декодирования JSON. Проверьте формат файла.")
        return 0.0

    # Вычисляем сумму произведений "score" и "weight"
    total = sum(item["score"] * item["weight"] for item in data)

    # Округляем результат до 3 знаков после запятой
    result = round(total, 3)

    return result


# Выводим результат
print(task())


