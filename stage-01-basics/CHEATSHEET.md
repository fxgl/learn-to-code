# Шпаргалка - Этап 1

Краткий справочник по основным операциям Python для соревнований.

---

## Ввод/Вывод

```python
# Одно число
n = int(input())

# Несколько чисел
a, b, c = map(int, input().split())

# Массив
arr = list(map(int, input().split()))

# N строк
lines = [input() for _ in range(n)]

# Вывод
print(result)
print(*arr)  # массив через пробел
print('\n'.join(map(str, arr)))  # столбиком
```

---

## Списки

```python
# Создание
arr = [0] * n
arr = [i for i in range(n)]
arr = [i**2 for i in range(n) if i % 2 == 0]

# Операции O(1)
arr.append(x)      # добавить в конец
arr.pop()          # удалить последний
arr[-1]            # последний элемент

# Операции O(n)
arr.insert(0, x)   # вставить в начало
arr.pop(0)         # удалить первый
arr.remove(x)      # удалить элемент x
x in arr           # проверка наличия

# Срезы
arr[1:4]           # [1,2,3]
arr[:3]            # первые 3
arr[3:]            # с 3-го до конца
arr[::-1]          # развернуть
arr[::2]           # каждый второй

# Полезное
sorted(arr)        # отсортированный
arr.sort()         # сортировать на месте
arr.sort(reverse=True)  # по убыванию
min(arr), max(arr), sum(arr)
arr.count(x)       # количество x
arr.index(x)       # индекс первого x
```

---

## Строки

```python
s = "Hello World"

# Методы
s.lower()          # "hello world"
s.upper()          # "HELLO WORLD"
s.strip()          # убрать пробелы по краям
s.split()          # ['Hello', 'World']
' '.join(words)    # склеить слова

# Проверки
s.isalpha()        # только буквы
s.isdigit()        # только цифры
s.isalnum()        # буквы и цифры
'abc' in s         # проверка подстроки

# Работа со символами
s[0]               # первый символ
s[-1]              # последний
s[::-1]            # развернуть
```

---

## Множества (Set)

```python
s = set()
s = {1, 2, 3}

# Операции O(1)
s.add(x)           # добавить
s.remove(x)        # удалить (KeyError если нет)
s.discard(x)       # удалить (без ошибки)
x in s             # проверка (БЫСТРО!)

# Операции над множествами
a | b              # объединение
a & b              # пересечение
a - b              # разность
a ^ b              # симметрическая разность

# Из списка
unique = set(arr)
```

---

## Словари (Dict)

```python
d = {}
d = {'key': 'value'}

# Операции O(1)
d[key] = value     # установить
val = d[key]       # получить (KeyError если нет)
val = d.get(key, default)  # с default значением
key in d           # проверка наличия
del d[key]         # удалить

# Итерация
for key in d:
    ...
for key, value in d.items():
    ...
for value in d.values():
    ...
```

---

## Counter

```python
from collections import Counter

arr = [1, 1, 2, 2, 2, 3]
count = Counter(arr)

count[1]           # 2 (частота)
count.most_common(2)  # [(2, 3), (1, 2)]
count.most_common(1)[0][0]  # самый частый элемент

# Можно со строками
Counter("hello")   # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```

---

## DefaultDict

```python
from collections import defaultdict

# Словарь с default значениями
d = defaultdict(int)     # default = 0
d = defaultdict(list)    # default = []
d = defaultdict(set)     # default = set()

# Не нужно проверять наличие ключа!
d['new_key'] += 1
d['fruits'].append('apple')
```

---

## Стек и Очередь

```python
# Стек (LIFO)
stack = []
stack.append(x)    # push
top = stack.pop()  # pop

# Очередь (FIFO) - используйте deque!
from collections import deque
queue = deque()
queue.append(x)       # enqueue
first = queue.popleft()  # dequeue

# Двусторонняя очередь
dq = deque()
dq.append(x)       # добавить справа
dq.appendleft(x)   # добавить слева
dq.pop()           # удалить справа
dq.popleft()       # удалить слева
```

---

## Сортировка

```python
# Стандартная
arr.sort()                    # на месте
sorted_arr = sorted(arr)      # новый список

# По убыванию
arr.sort(reverse=True)
sorted_arr = sorted(arr, reverse=True)

# По ключу
arr.sort(key=lambda x: x[1])  # по второму элементу
arr.sort(key=lambda x: -x)    # по убыванию (числа)
arr.sort(key=lambda x: (x[0], -x[1]))  # композитный ключ

# Примеры
points = [(1,5), (3,2), (2,8)]
points.sort(key=lambda p: p[0])  # по x
points.sort(key=lambda p: p[1])  # по y
points.sort(key=lambda p: p[0] + p[1])  # по сумме

words = ['cat', 'elephant', 'dog']
words.sort(key=len)  # по длине
```

---

## Бинарный поиск

```python
import bisect

arr = [1, 2, 4, 4, 5, 7, 9]  # ДОЛЖЕН быть отсортирован!

# Поиск позиции
bisect.bisect_left(arr, 4)   # 2 (первое вхождение)
bisect.bisect_right(arr, 4)  # 4 (после последнего)

# Вставка с сохранением порядка
bisect.insort(arr, 6)

# Проверка наличия
def binary_search_exists(arr, x):
    i = bisect.bisect_left(arr, x)
    return i < len(arr) and arr[i] == x

# Ручной бинарный поиск
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

## Два указателя

```python
# Классический паттерн
def two_pointers(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # логика
        if condition:
            left += 1
        else:
            right -= 1

# Быстрый/медленный указатель
def slow_fast(arr):
    slow = fast = 0

    while fast < len(arr):
        # логика
        slow += 1
        fast += 2

# Два указателя в двух массивах
def merge(arr1, arr2):
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
```

---

## Скользящее окно

```python
# Фиксированное окно
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Переменное окно
def variable_window(s, k):
    from collections import defaultdict

    char_count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Расширяем окно
        char_count[s[right]] += 1

        # Сжимаем если нужно
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

---

## Полезные функции

```python
# Enumerate - индекс и значение
for i, val in enumerate(arr):
    print(f"arr[{i}] = {val}")

# Zip - объединение последовательностей
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# All/Any
all([True, True, False])  # False
any([False, False, True])  # True

# Map
squared = list(map(lambda x: x**2, arr))
strings = list(map(str, arr))

# Filter
evens = list(filter(lambda x: x % 2 == 0, arr))

# Range
range(n)          # 0, 1, ..., n-1
range(1, n+1)     # 1, 2, ..., n
range(0, n, 2)    # 0, 2, 4, ..., n-1

# Comprehensions
[x for x in arr if x % 2 == 0]  # список
{x for x in arr}                # множество
{x: x**2 for x in arr}          # словарь
```

---

## Математика

```python
import math

# Основное
math.ceil(x)       # округление вверх
math.floor(x)      # округление вниз
math.sqrt(x)       # корень
abs(x)             # модуль

# Степени
x ** y             # x в степени y
pow(x, y, mod)     # (x^y) % mod (быстро!)

# НОД и НОК
math.gcd(a, b)     # НОД
def lcm(a, b):
    return (a * b) // math.gcd(a, b)

# Факториал
math.factorial(n)

# Константы
math.inf           # бесконечность
float('inf')       # то же самое
float('-inf')      # минус бесконечность
```

---

## Шаблон решения

```python
def solve():
    # Чтение данных
    n = int(input())
    arr = list(map(int, input().split()))

    # Решение
    result = 0

    # Вывод
    print(result)

# Один тест
solve()

# Несколько тестов
t = int(input())
for _ in range(t):
    solve()
```

---

## Сложность операций

### Список
| Операция | Сложность |
|----------|-----------|
| `arr[i]` | O(1) |
| `arr.append(x)` | O(1) |
| `arr.pop()` | O(1) |
| `arr.insert(0, x)` | O(n) |
| `arr.pop(0)` | O(n) |
| `x in arr` | O(n) |

### Множество/Словарь
| Операция | Сложность |
|----------|-----------|
| `x in s` | O(1) |
| `s.add(x)` | O(1) |
| `d[key]` | O(1) |
| `d[key] = val` | O(1) |

### Алгоритмы
| Алгоритм | Сложность |
|----------|-----------|
| Линейный поиск | O(n) |
| Бинарный поиск | O(log n) |
| Сортировка | O(n log n) |
| Два указателя | O(n) |
| Скользящее окно | O(n) |

---

## Типичные ошибки

❌ **Не делайте так:**
```python
# Создание матрицы
matrix = [[0] * m] * n  # ВСЕ строки - ОДИН список!

# Проверка в списке в цикле
for x in arr:
    if x in arr:  # O(n²) !
        ...

# Множественные проверки
if x == 1 or x == 2 or x == 3:  # длинно
```

✅ **Делайте так:**
```python
# Создание матрицы
matrix = [[0] * m for _ in range(n)]

# Проверка в множестве
s = set(arr)
for x in arr:
    if x in s:  # O(1) !
        ...

# Множественные проверки
if x in {1, 2, 3}:  # короче и быстрее
```

---

## Быстрые советы

1. **Используйте set для проверки "in"** — O(1) вместо O(n)
2. **Counter для подсчета частот** — проще и быстрее
3. **bisect для бинарного поиска** — не пишите вручную
4. **deque для очереди** — list.pop(0) медленный!
5. **enumerate для индексов** — читабельнее
6. **Списковые включения** — быстрее циклов
7. **defaultdict** — не проверяйте наличие ключа

---

**Сохраните эту шпаргалку и держите под рукой во время решения задач!** 📝
