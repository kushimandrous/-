import os

# Путь к твоему файлу
file_path = r"C:\Users\UserPC\Desktop\Новая папка (2)\log.txt"


def get_divisors_count(n):
    """Функция для подсчета количества всех делителей числа"""
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            if d * d == n:
                count += 1  # Если число - идеальный квадрат (например, 25 = 5*5)
            else:
                count += 2  # Считаем пару делителей (например, для 10 это 2 и 5)
        d += 1
    return count


# Создаем список для хранения 5 найденных чисел
results = []
# Начинаем с самого большого девятизначного числа
current_n = 999_999_999

# 'w' - режим записи (файл создастся или очистится при запуске)
with open(file_path, 'w', encoding='utf-8') as log:
    log.write("ОТЧЕТ О ПОИСКЕ ЧИСЕЛ ДЛЯ ЗАДАНИЯ 25\n")
    log.write("=" * 40 + "\n")

    while len(results) < 5:
        # 1. Считаем делители
        divs_count = get_divisors_count(current_n)

        # 2. Проверяем условие: (Число - КоличествоДелителей) должно делиться на 17
        difference = current_n - divs_count
        is_valid = (difference % 17 == 0)

        # 3. Логируем каждый шаг
        log.write(f"Проверка числа: {current_n}\n")
        log.write(f"  > Найдено делителей: {divs_count}\n")
        log.write(f"  > Разность ({current_n} - {divs_count}) = {difference}\n")

        if is_valid:
            log.write(f"  [!!!] УСПЕХ: {difference} делится на 17 без остатка!\n")
            results.append(current_n)
        else:
            log.write(f"  [x] ОТКАЗ: {difference} % 17 = {difference % 17} (остаток не 0)\n")

        log.write("-" * 20 + "\n")

        # Переходим к следующему числу вниз
        current_n -= 1

    # В конце записываем итоговый результат
    results.sort()  # Сортируем по возрастанию для ответа
    log.write("\nПОИСК ЗАВЕРШЕН!\n")
    log.write(f"Пять наибольших чисел в порядке возрастания: {results}\n")

print(f"Программа успешно завершена! Результаты и подробный лог ищи тут: {file_path}")
print(f"Итоговые числа: {results}")

