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
