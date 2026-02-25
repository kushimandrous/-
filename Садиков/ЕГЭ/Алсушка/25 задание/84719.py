from fnmatch import *

log_path = r"C:\Users\UserPC\Desktop\Новая папка (2)\log2.txt"

with open(log_path, 'w', encoding='utf-8') as log:
    log.write("Запуск перебора по кратности 2026...\n")

    # Чтобы не ждать вечность, я покажу логику на примере
    # Но в реальности цикл идет до 10**10
    found_count = 0
    for x in range(0, 10 ** 10, 2026):
        s_x = str(x)

        # Первая грубая проверка (чтобы не забивать лог всем подряд)
        if s_x[0]=='5':
            if fnmatch(s_x, '5?34?71*2'):
                log.write(f"Число {s_x} подошло под маску. Проверяем нечетность...\n")

                # Проверка нечетных позиций
                if s_x[1] in '13579' and s_x[4] in '13579':
                    log.write(f"!!! НАЙДЕНО: {s_x} полностью подходит !!!\n")
                    print(x)
                    found_count += 1

    log.write(f"\nПоиск завершен. Найдено чисел: {found_count}")

print("Готово!")