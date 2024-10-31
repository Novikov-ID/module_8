def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for item in numbers:
            try:
                result += item
            except TypeError:
                print(f"Некорректный тип данных для подсчёта суммы - {item}")
                incorrect_data += 1
        func_result = (result, incorrect_data)
        return func_result
    except TypeError:
        return None


def calculate_average(numbers):
    a = personal_sum(numbers)
    try:
        average = a[0] / (len(numbers) - a[1])
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
