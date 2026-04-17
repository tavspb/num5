import re

def get_positive_integer(
    min_value=1,
    max_value=10**9,
    max_length=10
):
    while True:
        user_input = input("Введите положительное целое число: ")

        # 1. Удаляем пробелы по краям
        user_input = user_input.strip()

        # 2. Проверка на пустой ввод
        if not user_input:
            print("Ошибка: ввод не может быть пустым.")
            continue

        # 3. Проверка длины
        if len(user_input) > max_length:
            print(f"Ошибка: число слишком длинное (максимум {max_length} символов).")
            continue

        # 4. Проверка формата (только цифры, без +, -, пробелов и т.п.)
        if not re.fullmatch(r"\d+", user_input):
            print("Ошибка: допускаются только цифры без пробелов и символов.")
            continue

        # 5. Проверка на ведущие нули (например 00123)
        if len(user_input) > 1 and user_input.startswith("0"):
            print("Ошибка: число не должно содержать ведущие нули.")
            continue

        try:
            number = int(user_input)
        except ValueError:
            print("Ошибка: не удалось преобразовать в число.")
            continue

        # 6. Проверка на ноль
        if number == 0:
            print("Ошибка: число должно быть больше нуля.")
            continue

        # 7. Проверка диапазона
        if number < min_value:
            print(f"Ошибка: число должно быть не меньше {min_value}.")
            continue

        if number > max_value:
            print(f"Ошибка: число должно быть не больше {max_value}.")
            continue

        return number


# Основная программа
num = get_positive_integer()
print(f"Вы ввели корректное число: {num}")
