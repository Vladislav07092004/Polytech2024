numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
s = sum(x for x in numbers if x is not None)
c = len(numbers)


m = s / c


n = [m if x is None else x for x in numbers]

print("Измененный список:", n)
