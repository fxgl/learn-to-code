# Этап 1: Основы Python и базовые алгоритмы

## Обзор

На этом этапе вы освоите синтаксис Python, необходимый для эффективного участия в соревнованиях по программированию, а также базовые структуры данных и алгоритмы.

**Время прохождения:** 2-3 недели
**Сложность:** Начальный уровень

---

## 1.1 Синтаксис Python для соревнований

### Быстрый ввод/вывод данных

В соревнованиях важна скорость чтения данных. Вот основные способы:

#### Чтение одного числа
```python
n = int(input())
```

#### Чтение нескольких чисел в одной строке
```python
# Способ 1: распаковка
a, b, c = map(int, input().split())

# Способ 2: в список
numbers = list(map(int, input().split()))
```

#### Чтение массива
```python
# Одна строка с числами
arr = list(map(int, input().split()))

# Несколько строк
n = int(input())
arr = [int(input()) for i in range(n)]
```

#### Быстрый вывод
```python
# Простой вывод
print(result)

# Вывод массива через пробел
print(*arr)

# Вывод массива через запятую
print(','.join(map(str, arr)))
```

### Работа со строками

```python
# Чтение строки
s = input()

# Без лидирующих/замыкающих пробелов
s = input().strip()

# Проверка на подстроку
if "abc" in s:
    print("Found")

# Разбиение строки
words = s.split()  # по пробелам
parts = s.split(',')  # по запятым

# Объединение строк
result = ' '.join(words)

# Преобразование регистра
upper = s.upper()
lower = s.lower()

# Проверка типов символов
s.isalpha()  # только буквы
s.isdigit()  # только цифры
s.isalnum()  # буквы и цифры
```

### Списковые включения (List Comprehensions)

Мощный инструмент для создания списков:

```python
# Создание списка квадратов
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# С условием
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Двумерный список (матрица)
matrix = [[0] * m for _ in range(n)]

# ВАЖНО: НЕ делайте так!
# matrix = [[0] * m] * n  # ВСЕ строки будут ссылаться на один список!

# Преобразование
strings = ['1', '2', '3']
numbers = [int(x) for x in strings]
```

### Полезные встроенные функции

```python
# Сортировка
arr = [3, 1, 4, 1, 5]
sorted_arr = sorted(arr)  # возвращает новый список
arr.sort()  # сортирует на месте

# Сортировка по ключу
arr.sort(key=lambda x: -x)  # по убыванию
arr.sort(reverse=True)  # тоже по убыванию

# Минимум и максимум
min_val = min(arr)
max_val = max(arr)

# Сумма
total = sum(arr)

# Подсчет элементов
count = arr.count(1)  # сколько раз встречается 1

# Индекс элемента
idx = arr.index(4)  # индекс первого вхождения 4

# Все/любой
all([True, True, False])  # False
any([False, False, True])  # True

# Zip - объединение списков
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Enumerate - индекс и элемент
for i, val in enumerate(arr):
    print(f"arr[{i}] = {val}")
```

### Примеры задач на ввод/вывод и строки

#### Задача 1: Way Too Long Words
**Платформа:** [Codeforces 71A](https://codeforces.com/problemset/problem/71/A) | **Сложность:** 800
**Условие:** Слова длиннее 10 символов сокращать до формата: первая буква + количество + последняя буква.

**Пример:**
```
Вход: localization
Выход: l10n

Вход: hello
Выход: hello (не сокращаем, т.к. <= 10)
```

**Решение:**
```python
def solve():
    word = input()

    if len(word) <= 10:
        print(word)
    else:
        # Первая + количество средних + последняя
        result = word[0] + str(len(word) - 2) + word[-1]
        print(result)

# Несколько тестов
t = int(input())
for _ in range(t):
    solve()
```

**Что здесь используется:**
- ✅ Чтение строки: `input()`
- ✅ Длина строки: `len(word)`
- ✅ Обращение к символам: `word[0]`, `word[-1]`
- ✅ Преобразование числа в строку: `str(...)`

---

#### Задача 2: Петя и строки
**Платформа:** [Codeforces 112A](https://codeforces.com/problemset/problem/112/A) | **Сложность:** 800
**Условие:** Сравнить две строки без учета регистра. Вывести:
- `-1` если первая меньше
- `0` если равны
- `1` если первая больше

**Решение:**
```python
s1 = input().lower()  # Приводим к нижнему регистру
s2 = input().lower()

if s1 < s2:
    print(-1)
elif s1 == s2:
    print(0)
else:
    print(1)
```

**Что здесь используется:**
- ✅ Преобразование регистра: `.lower()`
- ✅ Сравнение строк: `<`, `==`, `>`

---

#### Задача 3: Красивая матрица
**Платформа:** [Codeforces 263A](https://codeforces.com/problemset/problem/263/A) | **Сложность:** 800
**Условие:** Дана матрица 5×5 из 0 и одной 1. Найти минимальное количество ходов, чтобы переместить 1 в центр (позиция [2,2]).

**Решение:**
```python
# Читаем матрицу и находим позицию единицы
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            # Расстояние до центра (2, 2)
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
```

**Что здесь используется:**
- ✅ Чтение нескольких чисел: `list(map(int, input().split()))`
- ✅ Вложенные циклы
- ✅ Манхэттенское расстояние: `abs(x1 - x2) + abs(y1 - y2)`

---

## 1.2 Базовые структуры данных

### Списки (Lists)

Динамический массив - основная структура данных в Python:

```python
# Создание
arr = []
arr = [1, 2, 3, 4, 5]
arr = [0] * 10  # [0, 0, 0, ..., 0]

# Добавление
arr.append(6)  # в конец, O(1)
arr.insert(0, 0)  # в начало, O(n)

# Удаление
arr.pop()  # последний элемент, O(1)
arr.pop(0)  # первый элемент, O(n)
arr.remove(3)  # удалить элемент 3, O(n)

# Срезы
arr[1:4]  # элементы с индексами 1, 2, 3
arr[:3]  # первые 3 элемента
arr[3:]  # с 3-го до конца
arr[-1]  # последний элемент
arr[-3:]  # последние 3 элемента
arr[::-1]  # развернуть список

# Копирование
new_arr = arr.copy()  # или arr[:]
```

### Множества (Sets)

Неупорядоченная коллекция уникальных элементов:

```python
# Создание
s = set()
s = {1, 2, 3, 4, 5}
s = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Добавление и удаление
s.add(6)  # O(1)
s.remove(3)  # O(1), KeyError если нет
s.discard(3)  # O(1), не выдает ошибку

# Проверка принадлежности
if 5 in s:  # O(1) - очень быстро!
    print("Found")

# Операции над множествами
a = {1, 2, 3}
b = {3, 4, 5}
a | b  # объединение: {1, 2, 3, 4, 5}
a & b  # пересечение: {3}
a - b  # разность: {1, 2}
a ^ b  # симметрическая разность: {1, 2, 4, 5}
```

### Словари (Dictionaries)

Хэш-таблица для хранения пар ключ-значение:

```python
# Создание
d = {}
d = {'apple': 5, 'banana': 3}
d = dict()

# Доступ и изменение
d['apple'] = 10  # O(1)
val = d.get('apple', 0)  # получить с default значением
val = d['apple']  # KeyError если ключа нет

# Проверка наличия ключа
if 'apple' in d:  # O(1)
    print("Found")

# Удаление
del d['apple']
val = d.pop('banana', 0)  # удалить и вернуть значение

# Итерация
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Счетчик (очень полезно!)
from collections import Counter
arr = [1, 1, 2, 2, 2, 3]
count = Counter(arr)  # Counter({2: 3, 1: 2, 3: 1})
count[1]  # 2
count.most_common(2)  # [(2, 3), (1, 2)]

# defaultdict - словарь с default значением
from collections import defaultdict
d = defaultdict(int)  # default = 0
d['new_key'] += 1  # не нужно проверять наличие ключа
```

### Стек и Очередь

```python
from collections import deque

# Стек (LIFO - Last In First Out)
stack = []
stack.append(1)  # push
stack.append(2)
top = stack.pop()  # pop, вернет 2

# Очередь (FIFO - First In First Out)
queue = deque()
queue.append(1)  # enqueue в конец
queue.append(2)
first = queue.popleft()  # dequeue из начала, вернет 1

# Двусторонняя очередь (deque)
dq = deque([1, 2, 3])
dq.append(4)  # добавить справа
dq.appendleft(0)  # добавить слева
dq.pop()  # удалить справа
dq.popleft()  # удалить слева
```

### Примеры задач на структуры данных

#### Задача 4: Two Sum
**Платформа:** [LeetCode #1](https://leetcode.com/problems/two-sum/) | **Сложность:** Easy
**Условие:** Дан массив чисел и target. Найти индексы двух чисел, сумма которых равна target.

**Пример:**
```
Вход: nums = [2, 7, 11, 15], target = 9
Выход: [0, 1]
Объяснение: nums[0] + nums[1] = 2 + 7 = 9
```

**Наивное решение O(n²):**
```python
def two_sum_naive(nums, target):
    """Проверяем все пары - медленно!"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
```

**Оптимальное решение O(n) с использованием словаря:**
```python
def two_sum(nums, target):
    """Используем словарь для быстрого поиска"""
    seen = {}  # число -> его индекс

    for i, num in enumerate(nums):
        complement = target - num  # какое число нам нужно?

        if complement in seen:  # O(1) проверка!
            return [seen[complement], i]

        seen[num] = i  # запоминаем число и его индекс

    return None

# Тест
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # [0, 1]
```

**Что здесь используется:**
- ✅ Словарь для быстрого поиска: `O(1)` вместо `O(n)`
- ✅ `enumerate()` для получения индекса и значения
- ✅ Проверка наличия в словаре: `if key in dict`

---

#### Задача 5: Анаграммы
**Платформа:** [LeetCode #242](https://leetcode.com/problems/valid-anagram/) | **Сложность:** Easy
**Условие:** Проверить, являются ли две строки анаграммами (содержат одинаковые буквы).

**Пример:**
```
Вход: s = "anagram", t = "nagaram"
Выход: True
```

**Решение 1: Сортировка**
```python
def is_anagram_sort(s, t):
    """Простое решение через сортировку"""
    return sorted(s) == sorted(t)
```

**Решение 2: Counter (лучше для больших строк)**
```python
from collections import Counter

def is_anagram_counter(s, t):
    """Используем Counter для подсчета частот"""
    return Counter(s) == Counter(t)
```

**Решение 3: Словарь вручную**
```python
def is_anagram_dict(s, t):
    """Считаем частоты вручную"""
    if len(s) != len(t):
        return False

    count = {}

    # Считаем буквы в первой строке
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Вычитаем буквы из второй строки
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True
```

**Что здесь используется:**
- ✅ `sorted()` для сортировки строки
- ✅ `Counter` для подсчета частот
- ✅ Словарь с `get(key, default)`

---

#### Задача 6: Подсчет частоты
**Условие:** Дан массив чисел. Найти число, которое встречается чаще всего.
**Применение:** Часто встречается в задачах Codeforces Div 3/4

**Пример:**
```
Вход: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
Выход: 4
```

**Решение с Counter:**
```python
from collections import Counter

def most_frequent(arr):
    """Найти самый частый элемент"""
    count = Counter(arr)

    # most_common(1) возвращает [(элемент, частота)]
    return count.most_common(1)[0][0]

# Тест
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(most_frequent(arr))  # 4
```

**Решение без Counter:**
```python
def most_frequent_manual(arr):
    """Подсчет вручную"""
    freq = {}

    # Подсчитываем частоты
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Находим максимум
    max_count = 0
    result = None

    for num, count in freq.items():
        if count > max_count:
            max_count = count
            result = num

    return result
```

**Что здесь используется:**
- ✅ `Counter` - специализированный словарь для подсчета
- ✅ `most_common(n)` - топ-N элементов
- ✅ `.items()` для итерации по парам ключ-значение

---

#### Задача 7: Удалить дубликаты
**Платформа:** [LeetCode #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | **Сложность:** Easy
**Условие:** Удалить дубликаты из **отсортированного** массива in-place, вернуть новую длину.

**Пример:**
```
Вход: nums = [1, 1, 2, 2, 3]
Выход: 3 (nums становится [1, 2, 3, _, _])
```

**Решение с использованием set (создает новый массив):**
```python
def remove_duplicates_set(nums):
    """Простое решение через set"""
    unique = list(set(nums))
    unique.sort()  # set не сохраняет порядок!
    return unique
```

**Решение in-place (без дополнительной памяти):**
```python
def remove_duplicates_inplace(nums):
    """
    Удаляем дубликаты без нового массива
    Используем два указателя: read и write
    """
    if not nums:
        return 0

    write_pos = 1  # куда пишем уникальные элементы

    for read_pos in range(1, len(nums)):
        # Если элемент отличается от предыдущего
        if nums[read_pos] != nums[read_pos - 1]:
            nums[write_pos] = nums[read_pos]
            write_pos += 1

    return write_pos  # новая длина

# Тест
nums = [1, 1, 2, 2, 2, 3, 4, 4]
new_length = remove_duplicates_inplace(nums)
print(f"Новая длина: {new_length}")
print(f"Массив: {nums[:new_length]}")  # [1, 2, 3, 4]
```

**Что здесь используется:**
- ✅ `set` для получения уникальных элементов
- ✅ Техника двух указателей (read/write)
- ✅ Изменение массива in-place

---

#### Задача 8: Группировка анаграмм
**Платформа:** [LeetCode #49](https://leetcode.com/problems/group-anagrams/) | **Сложность:** Medium
**Условие:** Дан массив строк. Сгруппировать анаграммы вместе.

**Пример:**
```
Вход: ["eat", "tea", "tan", "ate", "nat", "bat"]
Выход: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

**Решение:**
```python
def group_anagrams(words):
    """
    Группируем анаграммы
    Ключ группы = отсортированные буквы
    """
    from collections import defaultdict

    groups = defaultdict(list)  # автоматически создает пустой список

    for word in words:
        # Сортируем буквы - это ключ для группы
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())

# Тест
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Что здесь используется:**
- ✅ `defaultdict(list)` - не нужно проверять наличие ключа
- ✅ `sorted()` для создания ключа группы
- ✅ `''.join()` для склеивания символов обратно в строку
- ✅ `.values()` для получения всех групп

---

## 1.3 Основные алгоритмы

### Линейный поиск

Поиск элемента в неотсортированном массиве:

```python
def linear_search(arr, target):
    """
    Поиск элемента в массиве
    Время: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # найден на позиции i
    return -1  # не найден

# Или просто:
if target in arr:  # O(n)
    idx = arr.index(target)
```

### Бинарный поиск

Поиск в **отсортированном** массиве:

```python
def binary_search(arr, target):
    """
    Бинарный поиск элемента
    Время: O(log n)
    Требование: массив должен быть отсортирован!
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # найден
        elif arr[mid] < target:
            left = mid + 1  # искать в правой половине
        else:
            right = mid - 1  # искать в левой половине

    return -1  # не найден

# Использование модуля bisect (рекомендуется!)
import bisect

arr = [1, 2, 4, 4, 5, 7, 9]

# Найти позицию для вставки
pos = bisect.bisect_left(arr, 4)  # 2 (первое вхождение)
pos = bisect.bisect_right(arr, 4)  # 4 (после последнего вхождения)

# Вставить элемент с сохранением сортировки
bisect.insort(arr, 6)
```

### Два указателя (Two Pointers)

Техника для работы с массивами и строками:

```python
def two_sum_sorted(arr, target):
    """
    Найти два числа в отсортированном массиве, сумма которых равна target
    Время: O(n)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # нужна большая сумма
        else:
            right -= 1  # нужна меньшая сумма

    return None

def remove_duplicates(arr):
    """
    Удалить дубликаты из отсортированного массива in-place
    Время: O(n)
    """
    if not arr:
        return 0

    write_idx = 1  # позиция для записи

    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[read_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1

    return write_idx  # новая длина массива
```

### Скользящее окно (Sliding Window)

Для задач с подмассивами фиксированной или переменной длины:

```python
def max_sum_subarray(arr, k):
    """
    Найти максимальную сумму подмассива длины k
    Время: O(n)
    """
    n = len(arr)
    if n < k:
        return None

    # Сумма первого окна
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Двигаем окно
    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

def longest_substring_k_distinct(s, k):
    """
    Найти длину самой длинной подстроки с максимум k различными символами
    Время: O(n)
    """
    from collections import defaultdict

    char_count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Расширяем окно
        char_count[s[right]] += 1

        # Сжимаем окно, если слишком много различных символов
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

### Примеры задач на алгоритмы

#### Задача 9: Maximum Subarray (Kadane's Algorithm)
**Платформа:** [LeetCode #53](https://leetcode.com/problems/maximum-subarray/) | **Сложность:** Medium
**Условие:** Найти подмассив с максимальной суммой.

**Пример:**
```
Вход: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Выход: 6
Объяснение: подмассив [4, -1, 2, 1] имеет сумму 6
```

**Наивное решение O(n²):**
```python
def max_subarray_naive(nums):
    """Проверяем все подмассивы - медленно!"""
    max_sum = float('-inf')

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum
```

**Алгоритм Кадане O(n):**
```python
def max_subarray_kadane(nums):
    """
    Алгоритм Кадане - очень важный алгоритм!
    Идея: на каждой позиции решаем - продолжить текущий подмассив
    или начать новый?
    """
    current_sum = nums[0]  # текущая сумма подмассива
    max_sum = nums[0]      # максимальная найденная сумма

    for i in range(1, len(nums)):
        # Либо добавляем к текущему, либо начинаем заново
        current_sum = max(nums[i], current_sum + nums[i])

        # Обновляем максимум
        max_sum = max(max_sum, current_sum)

    return max_sum

# Тест
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_kadane(nums))  # 6
```

**Что здесь используется:**
- ✅ Алгоритм Кадане - классический greedy подход
- ✅ Локальный vs глобальный максимум
- ✅ Время O(n) вместо O(n²)

---

#### Задача 10: Палиндром
**Платформа:** [LeetCode #125](https://leetcode.com/problems/valid-palindrome/) | **Сложность:** Easy
**Условие:** Проверить, является ли строка палиндромом (учитывать только буквы и цифры, игнорировать регистр).

**Пример:**
```
Вход: "A man, a plan, a canal: Panama"
Выход: True
```

**Решение с двумя указателями:**
```python
def is_palindrome(s):
    """
    Проверка палиндрома за O(n)
    Используем два указателя с концов строки
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Пропускаем не буквы/цифры слева
        while left < right and not s[left].isalnum():
            left += 1

        # Пропускаем не буквы/цифры справа
        while left < right and not s[right].isalnum():
            right -= 1

        # Сравниваем символы (без учета регистра)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Тест
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
```

**Альтернативное решение (проще, но медленнее):**
```python
def is_palindrome_simple(s):
    """Упрощенная версия"""
    # Оставляем только буквы и цифры, приводим к нижнему регистру
    clean = ''.join(c.lower() for c in s if c.isalnum())

    # Сравниваем с развернутой строкой
    return clean == clean[::-1]
```

**Что здесь используется:**
- ✅ Техника двух указателей
- ✅ Методы строк: `.isalnum()`, `.lower()`
- ✅ Срез для разворота: `[::-1]`

---

#### Задача 11: Container With Most Water
**Платформа:** [LeetCode #11](https://leetcode.com/problems/container-with-most-water/) | **Сложность:** Medium
**Условие:** Дан массив высот вертикальных линий. Найти две линии, которые вместе с осью X образуют контейнер с максимальным объемом воды.

**Пример:**
```
Вход: [1, 8, 6, 2, 5, 4, 8, 3, 7]
Выход: 49
Объяснение: линии на позициях 1 и 8 (высоты 8 и 7)
Площадь = ширина × min(высоты) = 7 × 7 = 49
```

**Решение с двумя указателями:**
```python
def max_area(height):
    """
    Используем два указателя с концов
    Всегда двигаем указатель с меньшей высотой
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Вычисляем площадь
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        max_water = max(max_water, area)

        # Двигаем указатель с меньшей высотой
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Тест
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(heights))  # 49
```

**Почему двигаем меньший указатель?**
- Ширина всегда уменьшается при движении
- Единственный шанс улучшить площадь - увеличить высоту
- Двигая больший указатель, высота может только уменьшиться!

**Что здесь используется:**
- ✅ Техника двух указателей
- ✅ Greedy выбор (двигаем меньший)
- ✅ Время O(n) вместо O(n²)

---

#### Задача 12: Longest Substring Without Repeating Characters
**Платформа:** [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | **Сложность:** Medium
**Условие:** Найти длину самой длинной подстроки без повторяющихся символов.

**Пример:**
```
Вход: "abcabcbb"
Выход: 3
Объяснение: "abc"
```

**Решение со скользящим окном:**
```python
def longest_substring_no_repeats(s):
    """
    Скользящее окно с хэш-таблицей
    Храним последнюю позицию каждого символа
    """
    char_index = {}  # символ -> его последняя позиция
    left = 0         # левая граница окна
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        # Если символ уже встречался в текущем окне
        if char in char_index and char_index[char] >= left:
            # Сдвигаем левую границу
            left = char_index[char] + 1

        # Обновляем позицию символа
        char_index[char] = right

        # Обновляем максимальную длину
        max_length = max(max_length, right - left + 1)

    return max_length

# Тесты
print(longest_substring_no_repeats("abcabcbb"))  # 3 ("abc")
print(longest_substring_no_repeats("bbbbb"))     # 1 ("b")
print(longest_substring_no_repeats("pwwkew"))    # 3 ("wke")
```

**Что здесь используется:**
- ✅ Скользящее окно переменного размера
- ✅ Словарь для отслеживания позиций символов
- ✅ Время O(n), память O(min(n, m)) где m - размер алфавита

---

#### Задача 13: Maximum Sum Subarray of Size K
**Условие:** Найти максимальную сумму подмассива длины K.

**Пример:**
```
Вход: arr = [2, 1, 5, 1, 3, 2], k = 3
Выход: 9
Объяснение: [5, 1, 3] имеет сумму 9
```

**Решение со скользящим окном:**
```python
def max_sum_subarray(arr, k):
    """
    Скользящее окно фиксированного размера
    Время: O(n) вместо O(n*k)
    """
    n = len(arr)
    if n < k:
        return None

    # Сумма первого окна
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Скользим окно: убираем левый, добавляем правый
    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Тест
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # 9
```

**Почему это быстрее?**
```python
# Наивный подход O(n*k):
for i in range(n - k + 1):
    current_sum = sum(arr[i:i+k])  # каждый раз заново считаем!

# Скользящее окно O(n):
window_sum = sum(arr[:k])
for i in range(k, n):
    window_sum = window_sum - arr[i-k] + arr[i]  # только 2 операции!
```

**Что здесь используется:**
- ✅ Фиксированное скользящее окно
- ✅ Повторное использование предыдущих вычислений
- ✅ Оптимизация O(n*k) → O(n)

---

#### Задача 14: Первое и последнее вхождение
**Платформа:** [LeetCode #34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | **Сложность:** Medium
**Условие:** Найти первое и последнее вхождение элемента в отсортированном массиве.

**Пример:**
```
Вход: nums = [5, 7, 7, 8, 8, 10], target = 8
Выход: [3, 4]
```

**Решение с bisect:**
```python
import bisect

def find_first_last(nums, target):
    """
    Используем бинарный поиск
    bisect_left - первое вхождение
    bisect_right - позиция после последнего
    """
    left = bisect.bisect_left(nums, target)

    # Проверяем, есть ли элемент вообще
    if left == len(nums) or nums[left] != target:
        return [-1, -1]

    right = bisect.bisect_right(nums, target) - 1

    return [left, right]

# Тест
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(find_first_last(nums, target))  # [3, 4]
```

**Решение с ручным бинарным поиском:**
```python
def find_first_last_manual(nums, target):
    """
    Два бинарных поиска:
    1) Ищем первое вхождение
    2) Ищем последнее вхождение
    """
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid       # нашли, но продолжаем искать левее
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid       # нашли, но продолжаем искать правее
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    first = find_first(nums, target)
    if first == -1:
        return [-1, -1]

    last = find_last(nums, target)
    return [first, last]
```

**Что здесь используется:**
- ✅ Модуль `bisect` для бинарного поиска
- ✅ Модифицированный бинарный поиск (ищем границы)
- ✅ Время O(log n)

---

## Практические задачи

### Уровень 1 (Легкие)

1. **Сумма двух чисел**
   - Дан массив и число target. Найти два числа, сумма которых равна target
   - Платформы: LeetCode #1, Codeforces

2. **Палиндром**
   - Проверить, является ли строка палиндромом
   - Платформы: LeetCode #125

3. **Анаграммы**
   - Проверить, являются ли две строки анаграммами
   - Платформы: LeetCode #242

4. **Подсчет частоты элементов**
   - Найти элемент, встречающийся чаще всего
   - Платформы: Codeforces Div 3/4

5. **Уникальные элементы**
   - Удалить дубликаты из массива
   - Платформы: LeetCode #26

### Уровень 2 (Средние)

1. **Максимальная сумма подмассива**
   - Найти подмассив с максимальной суммой (алгоритм Кадане)
   - Платформы: LeetCode #53

2. **Товары со скидкой**
   - Найти для каждого товара следующий более дешевый товар справа
   - Платформы: LeetCode #739 (Next Greater Element)

3. **Скользящее окно максимум**
   - Найти максимум в каждом окне размера k
   - Платформы: LeetCode #239

4. **Длина самой длинной подстроки без повторов**
   - Платформы: LeetCode #3

5. **Сортировка по частоте**
   - Отсортировать элементы по частоте встречаемости
   - Платформы: LeetCode #451

---

## Шаблон для решения задач

Используйте этот шаблон как основу:

```python
def solve():
    # Чтение входных данных
    n = int(input())
    arr = list(map(int, input().split()))

    # Ваше решение здесь
    result = 0

    # Вывод результата
    print(result)

# Для одного теста
solve()

# Для нескольких тестов
# t = int(input())
# for _ in range(t):
#     solve()
```

---

## Советы

1. **Используйте списковые включения** - они быстрее циклов
2. **Используйте встроенные функции** - они оптимизированы на C уровне
3. **Избегайте лишних копирований** - работайте с индексами где возможно
4. **Используйте set для проверки принадлежности** - O(1) вместо O(n)
5. **Учите стандартную библиотеку** - `collections`, `itertools`, `bisect`

---

## Следующие шаги

После освоения этого этапа:
1. Решите 15-20 задач уровня 1
2. Решите 10-15 задач уровня 2
3. Переходите к **Этапу 2: Математика и жадные алгоритмы**

Примеры кода с задачами находятся в папке `examples/`.
