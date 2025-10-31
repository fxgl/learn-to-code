"""
Алгоритмы поиска

Линейный поиск - O(n)
Бинарный поиск - O(log n) - работает только на отсортированных массивах!
"""

# ============================================
# Линейный поиск
# ============================================
print("=== ЛИНЕЙНЫЙ ПОИСК ===")
print("Просто идем по массиву и ищем нужный элемент\n")

def linear_search(arr, target):
    """
    Поиск элемента в массиве
    Время: O(n) - в худшем случае проверим все элементы
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # нашли!
    return -1  # не нашли

# Пример
arr = [10, 23, 45, 70, 11, 15]
target = 70

result = linear_search(arr, target)
print(f"Массив: {arr}")
print(f"Ищем: {target}")
if result != -1:
    print(f"Найдено на позиции: {result}")
else:
    print("Не найдено")

# В Python можно просто:
if target in arr:
    idx = arr.index(target)
    print(f"Используя index(): {idx}")

# ============================================
# Бинарный поиск (Binary Search)
# ============================================
print("\n\n=== БИНАРНЫЙ ПОИСК ===")
print("Работает ТОЛЬКО на отсортированном массиве!")
print("Каждый раз делим массив пополам\n")

def binary_search(arr, target):
    """
    Бинарный поиск элемента
    Время: O(log n) - ОЧЕНЬ быстро!
    ВАЖНО: массив должен быть отсортирован!
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Находим середину
        mid = (left + right) // 2

        print(f"  Проверяем: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target:
            return mid  # нашли!

        elif arr[mid] < target:
            # Искомое число больше, ищем в правой половине
            left = mid + 1

        else:
            # Искомое число меньше, ищем в левой половине
            right = mid - 1

    return -1  # не нашли

# Пример
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

print(f"Отсортированный массив: {arr}")
print(f"Ищем: {target}\n")

result = binary_search(arr, target)
if result != -1:
    print(f"\nНайдено на позиции: {result}")
else:
    print("\nНе найдено")

# ============================================
# Модуль bisect (рекомендуется!)
# ============================================
print("\n\n=== МОДУЛЬ BISECT ===")
print("В Python есть готовый модуль для бинарного поиска\n")

import bisect

arr = [1, 2, 4, 4, 4, 5, 7, 9]
print(f"Массив: {arr}\n")

# bisect_left - позиция для вставки (слева от существующих)
pos = bisect.bisect_left(arr, 4)
print(f"bisect_left(arr, 4) = {pos}")
print(f"  → первое вхождение 4 на позиции {pos}")

# bisect_right - позиция для вставки (справа от существующих)
pos = bisect.bisect_right(arr, 4)
print(f"bisect_right(arr, 4) = {pos}")
print(f"  → после последнего вхождения 4")

# Проверка наличия элемента
def binary_search_exists(arr, target):
    """Проверить, есть ли элемент в отсортированном массиве"""
    i = bisect.bisect_left(arr, target)
    return i < len(arr) and arr[i] == target

print(f"\n4 есть в массиве? {binary_search_exists(arr, 4)}")
print(f"6 есть в массиве? {binary_search_exists(arr, 6)}")

# Вставка с сохранением порядка
arr = [1, 3, 5, 7, 9]
bisect.insort(arr, 4)
print(f"\nПосле insort(arr, 4): {arr}")

# ============================================
# Бинарный поиск по ответу
# ============================================
print("\n\n=== БИНАРНЫЙ ПОИСК ПО ОТВЕТУ ===")
print("Ищем не элемент, а оптимальное значение\n")

def find_square_root(n, precision=0.0001):
    """
    Найти квадратный корень с заданной точностью
    Используем бинарный поиск!
    """
    left, right = 0, n

    while right - left > precision:
        mid = (left + right) / 2

        if mid * mid < n:
            left = mid
        else:
            right = mid

    return (left + right) / 2

n = 10
result = find_square_root(n)
print(f"Квадратный корень из {n} ≈ {result:.4f}")
print(f"Проверка: {result:.4f}^2 = {result**2:.4f}")

# Задача: найти минимальное K, чтобы можно было съесть все бананы
def can_eat_all_bananas(piles, k, hours):
    """Проверить, можно ли съесть все бананы за hours часов со скоростью k"""
    time_needed = 0
    for pile in piles:
        time_needed += (pile + k - 1) // k  # округление вверх
    return time_needed <= hours

def min_eating_speed(piles, hours):
    """Найти минимальную скорость поедания бананов"""
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2

        if can_eat_all_bananas(piles, mid, hours):
            right = mid  # можем медленнее
        else:
            left = mid + 1  # нужно быстрее

    return left

piles = [3, 6, 7, 11]
hours = 8
result = min_eating_speed(piles, hours)
print(f"\nКучи бананов: {piles}")
print(f"Есть {hours} часов")
print(f"Минимальная скорость: {result} бананов/час")

# ============================================
# Техника двух указателей (Two Pointers)
# ============================================
print("\n\n=== ТЕХНИКА ДВУХ УКАЗАТЕЛЕЙ ===")
print("Используем два указателя для эффективного решения задач\n")

def two_sum_sorted(arr, target):
    """
    Найти два числа в ОТСОРТИРОВАННОМ массиве, дающие target
    Время: O(n)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        print(f"  left={left}({arr[left]}), right={right}({arr[right]}), sum={current_sum}")

        if current_sum == target:
            return [left, right]

        elif current_sum < target:
            left += 1  # нужна большая сумма

        else:
            right -= 1  # нужна меньшая сумма

    return None

arr = [1, 2, 3, 4, 6, 8, 9]
target = 10

print(f"Отсортированный массив: {arr}")
print(f"Ищем два числа, сумма = {target}\n")

result = two_sum_sorted(arr, target)
if result:
    print(f"\nНашли: индексы {result}")
    print(f"Числа: {arr[result[0]]} + {arr[result[1]]} = {target}")

# Задача: удалить дубликаты из отсортированного массива
def remove_duplicates(arr):
    """
    Удалить дубликаты in-place (не создавая новый массив)
    Вернуть новую длину
    """
    if not arr:
        return 0

    write_pos = 1  # куда пишем

    for read_pos in range(1, len(arr)):
        # Если элемент отличается от предыдущего
        if arr[read_pos] != arr[read_pos - 1]:
            arr[write_pos] = arr[read_pos]
            write_pos += 1

    return write_pos

arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print(f"\nМассив с дубликатами: {arr}")
new_length = remove_duplicates(arr)
print(f"После удаления дубликатов: {arr[:new_length]}")

# Задача: проверка палиндрома
def is_palindrome(s):
    """Проверить, является ли строка палиндромом"""
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

s1 = "radar"
s2 = "hello"
print(f"\n'{s1}' - палиндром? {is_palindrome(s1)}")
print(f"'{s2}' - палиндром? {is_palindrome(s2)}")

# Задача: контейнер с наибольшим объемом воды
def max_area(height):
    """
    Дан массив высот. Найти максимальную площадь между двумя линиями
    """
    left = 0
    right = len(height) - 1
    max_area_val = 0

    while left < right:
        # Площадь = ширина × минимальная высота
        width = right - left
        area = width * min(height[left], height[right])
        max_area_val = max(max_area_val, area)

        # Двигаем указатель с меньшей высотой
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area_val

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(heights)
print(f"\nВысоты: {heights}")
print(f"Максимальная площадь: {result}")

# ============================================
# Задачи для практики
# ============================================
print("\n\n=== ЗАДАЧИ ДЛЯ ПРАКТИКИ ===")

# 1. Найти первое и последнее вхождение элемента в отсортированном массиве
def find_first_last(arr, target):
    """Найти первое и последнее вхождение"""
    first = bisect.bisect_left(arr, target)
    last = bisect.bisect_right(arr, target) - 1

    if first < len(arr) and arr[first] == target:
        return [first, last]
    return [-1, -1]

arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
result = find_first_last(arr, target)
print(f"\nМассив: {arr}, ищем: {target}")
print(f"Первое и последнее вхождение: {result}")

# 2. Три суммы равны target
def three_sum(arr, target):
    """Найти три числа, сумма которых равна target"""
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        # Используем two pointers для оставшихся двух
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 15
result = three_sum(arr, target)
print(f"\nМассив: {arr}, target: {target}")
print(f"Тройки чисел с суммой {target}:")
for triplet in result[:5]:  # показываем первые 5
    print(f"  {triplet}")

print("\n=== Конец примеров ===")
print("\nВАЖНО помнить:")
print("✓ Бинарный поиск работает только на отсортированных данных")
print("✓ Бинарный поиск: O(log n) vs Линейный поиск: O(n)")
print("✓ Два указателя часто используется с отсортированными массивами")
print("✓ Бинарный поиск по ответу - мощная техника оптимизации")
