"""
Техника скользящего окна (Sliding Window)

Используется для задач с подмассивами или подстроками.
Вместо проверки каждого подмассива заново (O(n²)),
мы "скользим" окном по массиву (O(n)).
"""

# ============================================
# Фиксированное окно
# ============================================
print("=== ФИКСИРОВАННОЕ ОКНО ===")
print("Окно постоянного размера двигается по массиву\n")

def max_sum_subarray(arr, k):
    """
    Найти максимальную сумму подмассива размера k
    Время: O(n) вместо O(n*k)
    """
    n = len(arr)
    if n < k:
        return None

    # Вычисляем сумму первого окна
    window_sum = sum(arr[:k])
    max_sum = window_sum

    print(f"Начальное окно {arr[:k]}, сумма = {window_sum}")

    # Двигаем окно
    for i in range(k, n):
        # Убираем левый элемент, добавляем правый
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

        print(f"Окно {arr[i-k+1:i+1]}, сумма = {window_sum}")

    return max_sum

# Пример
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

print(f"Массив: {arr}")
print(f"Размер окна: {k}\n")

result = max_sum_subarray(arr, k)
print(f"\nМаксимальная сумма: {result}")

# ============================================
# Переменное окно
# ============================================
print("\n\n=== ПЕРЕМЕННОЕ ОКНО ===")
print("Размер окна меняется в зависимости от условия\n")

def longest_substring_k_distinct(s, k):
    """
    Найти длину самой длинной подстроки с максимум k различными символами
    Время: O(n)
    """
    from collections import defaultdict

    char_count = defaultdict(int)
    left = 0
    max_length = 0

    print(f"Строка: '{s}', k = {k}\n")

    for right in range(len(s)):
        # Расширяем окно вправо
        char_count[s[right]] += 1

        print(f"Добавили '{s[right]}', окно: '{s[left:right+1]}', "
              f"уникальных: {len(char_count)}")

        # Сжимаем окно слева, если слишком много уникальных
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

            print(f"  → Сжали окно: '{s[left:right+1]}', "
                  f"уникальных: {len(char_count)}")

        # Обновляем максимум
        max_length = max(max_length, right - left + 1)

    return max_length

s = "eceba"
k = 2
result = longest_substring_k_distinct(s, k)
print(f"\nМаксимальная длина: {result}")

# ============================================
# Классические задачи
# ============================================
print("\n\n=== КЛАССИЧЕСКИЕ ЗАДАЧИ ===\n")

# Задача 1: Максимум в каждом окне
def max_in_windows(arr, k):
    """
    Найти максимум в каждом окне размера k
    """
    from collections import deque

    result = []
    dq = deque()  # храним индексы

    for i in range(len(arr)):
        # Удаляем элементы вне окна
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Удаляем меньшие элементы (они бесполезны)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # Добавляем результат когда окно заполнено
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = max_in_windows(arr, k)
print(f"Задача 1: Максимум в окне")
print(f"Массив: {arr}")
print(f"Размер окна: {k}")
print(f"Максимумы: {result}")

# Задача 2: Минимальная длина подмассива с суммой ≥ target
def min_subarray_sum(arr, target):
    """
    Найти минимальную длину подмассива с суммой ≥ target
    """
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        # Сжимаем окно пока сумма ≥ target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0

arr = [2, 3, 1, 2, 4, 3]
target = 7
result = min_subarray_sum(arr, target)
print(f"\nЗадача 2: Минимальная длина с суммой ≥ {target}")
print(f"Массив: {arr}")
print(f"Минимальная длина: {result}")

# Задача 3: Самая длинная подстрока без повторов
def longest_substring_no_repeats(s):
    """
    Найти длину самой длинной подстроки без повторяющихся символов
    """
    char_index = {}  # символ -> последний индекс
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Если символ уже встречался в текущем окне
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"
result = longest_substring_no_repeats(s)
print(f"\nЗадача 3: Подстрока без повторов")
print(f"Строка: '{s}'")
print(f"Максимальная длина: {result}")

# Задача 4: Подстрока со всеми символами
def min_window_substring(s, t):
    """
    Найти минимальную подстроку s, содержащую все символы из t
    """
    from collections import Counter

    if not s or not t:
        return ""

    # Подсчитываем символы в t
    target_count = Counter(t)
    required = len(target_count)

    # Счетчик для окна
    window_count = {}
    formed = 0  # сколько уникальных символов совпало

    left = 0
    min_length = float('inf')
    min_left = 0

    for right in range(len(s)):
        # Добавляем символ справа
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        # Проверяем, достигли ли нужного количества этого символа
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Сжимаем окно пока все символы присутствуют
        while formed == required and left <= right:
            # Обновляем результат
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left

            # Убираем левый символ
            char = s[left]
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1

            left += 1

    return "" if min_length == float('inf') else s[min_left:min_left + min_length]

s = "ADOBECODEBANC"
t = "ABC"
result = min_window_substring(s, t)
print(f"\nЗадача 4: Минимальное окно")
print(f"Строка s: '{s}'")
print(f"Строка t: '{t}'")
print(f"Минимальное окно: '{result}'")

# ============================================
# Задача 5: Подмассивы с K различными элементами
# ============================================
def subarrays_k_distinct(arr, k):
    """
    Подсчитать количество подмассивов ровно с K различными элементами
    Хитрость: at_most(k) - at_most(k-1)
    """
    def at_most_k_distinct(arr, k):
        """Подмассивы с максимум k различными элементами"""
        from collections import defaultdict

        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(arr)):
            count[arr[right]] += 1

            while len(count) > k:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    del count[arr[left]]
                left += 1

            # Все подмассивы, заканчивающиеся в right
            result += right - left + 1

        return result

    return at_most_k_distinct(arr, k) - at_most_k_distinct(arr, k - 1)

arr = [1, 2, 1, 2, 3]
k = 2
result = subarrays_k_distinct(arr, k)
print(f"\nЗадача 5: Подмассивы с {k} различными")
print(f"Массив: {arr}")
print(f"Количество подмассивов: {result}")

# ============================================
# Задача 6: Фрукты в корзинах
# ============================================
def total_fruit(fruits):
    """
    Собрать максимум фруктов, имея 2 корзины (каждая для одного типа)
    По сути - longest_substring_k_distinct с k=2
    """
    from collections import defaultdict

    basket = defaultdict(int)
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
        basket[fruits[right]] += 1

        # Если больше 2 типов, убираем слева
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

fruits = [1, 2, 1, 2, 3, 1, 1]
result = total_fruit(fruits)
print(f"\nЗадача 6: Фрукты в корзинах")
print(f"Фрукты: {fruits}")
print(f"Максимум фруктов: {result}")

# ============================================
# Шаблон для скользящего окна
# ============================================
print("\n\n=== ШАБЛОН ДЛЯ СКОЛЬЗЯЩЕГО ОКНА ===")
print("""
# Фиксированное окно
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    result = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        result = max(result, window_sum)  # или другая операция

    return result

# Переменное окно
def variable_window(arr):
    left = 0
    result = 0

    for right in range(len(arr)):
        # Добавляем arr[right] в окно

        # Сжимаем окно пока условие нарушено
        while condition_violated:
            # Убираем arr[left] из окна
            left += 1

        # Обновляем результат
        result = max(result, right - left + 1)

    return result
""")

print("\n=== Конец примеров ===")
print("\nВАЖНО помнить:")
print("✓ Скользящее окно: O(n) вместо O(n²)")
print("✓ Фиксированное окно: размер постоянный")
print("✓ Переменное окно: размер меняется по условию")
print("✓ Используйте два указателя: left и right")
print("✓ Часто нужен словарь для подсчета элементов в окне")
