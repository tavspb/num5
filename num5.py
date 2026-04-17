"""
Модуль для ввода и валидации положительного целого числа.

Предоставляет функцию get_positive_integer() для безопасного получения
от пользователя положительного целого числа с обработкой ошибок.
"""

def is_positive_integer(value: str) -> bool:
    """
    Проверяет, является ли строка положительным целым числом.
    
    Args:
        value (str): Строка для проверки
        
    Returns:
        bool: True, если строка представляет положительное целое число, иначе False
    """
    try:
        number = int(value)
        return number > 0
    except ValueError:
        return False


def get_positive_integer(prompt: str = "Введите положительное целое число: ",
                         error_message: str = "Ошибка: Введите положительное целое число!",
                         min_value: int = 1,
                         max_value: int = None) -> int:
    """
    Запрашивает у пользователя положительное целое число до тех пор,
    пока не будет введено корректное значение.
    
    Args:
        prompt (str): Сообщение для запроса ввода
        error_message (str): Сообщение об ошибке при неверном вводе
        min_value (int): Минимальное допустимое значение (по умолчанию 1)
        max_value (int, optional): Максимальное допустимое значение
        
    Returns:
        int: Корректно введённое положительное целое число
        
    Example:
        >>> age = get_positive_integer("Введите ваш возраст: ", min_value=1, max_value=120)
        >>> print(f"Ваш возраст: {age}")
    """
    while True:
        try:
            # Получение ввода от пользователя
            user_input = input(prompt).strip()
            
            # Проверка на пустой ввод
            if not user_input:
                print("Ошибка: Ввод не может быть пустым!")
                continue
            
            # Преобразование в целое число
            number = int(user_input)
            
            # Проверка на положительность
            if number <= 0:
                print(f"Ошибка: Число должно быть положительным (больше 0)!")
                continue
            
            # Проверка минимального значения
            if number < min_value:
                print(f"Ошибка: Число должно быть не меньше {min_value}!")
                continue
            
            # Проверка максимального значения (если задано)
            if max_value is not None and number > max_value:
                print(f"Ошибка: Число должно быть не больше {max_value}!")
                continue
            
            # Все проверки пройдены - возвращаем число
            return number
            
        except ValueError:
            # Обработка нечислового ввода
            print(error_message)


# Дополнительная функция для демонстрации расширяемости
def get_integer_in_range(min_val: int, max_val: int, 
                        prompt: str = None) -> int:
    """
    Расширенная версия: запрашивает целое число в заданном диапазоне.
    
    Args:
        min_val (int): Минимальное значение (включительно)
        max_val (int): Максимальное значение (включительно)
        prompt (str, optional): Пользовательское сообщение
        
    Returns:
        int: Число в диапазоне [min_val, max_val]
    """
    if prompt is None:
        prompt = f"Введите целое число от {min_val} до {max_val}: "
    
    return get_positive_integer(
        prompt=prompt,
        min_value=min_val,
        max_value=max_val
    )


# Модульные тесты
def run_tests():
    """Запускает набор тестов для проверки функций валидации."""
    
    print("=" * 50)
    print("ЗАПУСК ТЕСТОВ ВАЛИДАЦИИ")
    print("=" * 50)
    
    # Тест 1: Проверка is_positive_integer
    print("\nТест 1: Функция is_positive_integer()")
    test_cases = [
        ("5", True),      # положительное целое
        ("0", False),     # ноль
        ("-3", False),    # отрицательное
        ("abc", False),   # текст
        ("12.5", False),  # дробное
        ("", False),      # пустая строка
        ("  10  ", True), # с пробелами
        ("100", True),    # большое число
    ]
    
    for input_val, expected in test_cases:
        result = is_positive_integer(input_val)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_positive_integer('{input_val}') -> {result} (ожидалось: {expected})")
    
    # Тест 2: Проверка get_positive_integer с имитацией ввода
    print("\nТест 2: Имитация ввода (только логика, без реального input)")
    print("Для ручного тестирования запустите программу отдельно.")
    
    print("\n" + "=" * 50)
    print("ТЕСТЫ ЗАВЕРШЕНЫ")
    print("=" * 50)


# Основная программа
def main():
    """Основная функция программы."""
    
    print("\n" + "=" * 60)
    print("ПРОГРАММА ВВОДА ПОЛОЖИТЕЛЬНОГО ЦЕЛОГО ЧИСЛА")
    print("=" * 60)
    
    # Базовый пример: просто положительное целое число
    print("\n[Пример 1] Базовый ввод:")
    number1 = get_positive_integer()
    print(f"Вы ввели: {number1}")
    
    # Пример с дополнительными проверками диапазона
    print("\n[Пример 2] Ввод с ограничением диапазона (1-100):")
    number2 = get_positive_integer(
        prompt="Введите число от 1 до 100: ",
        min_value=1,
        max_value=100
    )
    print(f"Вы ввели: {number2}")
    
    # Пример использования расширенной функции
    print("\n[Пример 3] Использование get_integer_in_range():")
    number3 = get_integer_in_range(10, 50, "Введите число от 10 до 50: ")
    print(f"Вы ввели: {number3}")
    
    print("\n" + "=" * 60)
    print("ПРОГРАММА ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    # Запуск тестов
    run_tests()
    
    # Запуск основной программы
    print("\n" + "=" * 60)
    print("РУЧНОЕ ТЕСТИРОВАНИЕ")
    print("=" * 60)
    print("\nПопробуйте ввести разные значения:")
    print("- Текст (например, 'abc')")
    print("- Отрицательные числа (например, -5)")
    print("- Ноль (0)")
    print("- Пустую строку")
    print("- Корректные числа (например, 42)")
    print("-" * 60)
    
    main()