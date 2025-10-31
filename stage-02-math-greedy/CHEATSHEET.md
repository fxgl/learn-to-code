# Шпаргалка - Этап 2: Математика и жадные алгоритмы

Быстрый справочник по всем операциям, формулам и паттернам этапа 2.

---

## 📐 Математика

### НОД и НОК

```python
import math

# НОД (наибольший общий делитель)
gcd = math.gcd(12, 18)  # 6

# НОК (наименьшее общее кратное)
lcm = (a * b) // math.gcd(a, b)

# НОД массива
from functools import reduce
nums = [12, 18, 24]
gcd_array = reduce(math.gcd, nums)  # 6

# Алгоритм Евклида (ручная реализация)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Расширенный алгоритм Евклида
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
```

### Простые числа

```python
# Проверка на простоту (наивная)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Решето Эратосфена (до N)
def sieve(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p < n:
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1

    return [i for i in range(n) if is_prime[i]]

# Разложение на простые множители
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Количество делителей
def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1 if i * i == n else 2
        i += 1
    return count
```

### Модульная арифметика

```python
# Базовые операции
MOD = 10**9 + 7

add = (a + b) % MOD
sub = (a - b + MOD) % MOD  # +MOD для положительного результата
mul = (a * b) % MOD

# Модульное возведение в степень
pow(a, b, MOD)  # встроенная функция

# Ручная реализация
def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Модульное деление (через обратный элемент)
def mod_div(a, b, mod):
    # a/b mod m = a * b^(-1) mod m
    # b^(-1) = b^(m-2) mod m (если m простое, по теореме Ферма)
    return (a * pow(b, mod - 2, mod)) % mod
```

### Быстрое возведение в степень

```python
# Встроенная функция
result = pow(2, 10)        # 1024
result = pow(2, 10, 1000)  # 24 (с модулем)

# Рекурсивная реализация
def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

# Итеративная (битовая)
def power_iterative(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    current = x

    while n > 0:
        if n % 2 == 1:
            result *= current
        current *= current
        n //= 2

    return result
```

### Факториалы и комбинаторика

```python
import math

# Факториал
factorial = math.factorial(5)  # 120

# Биномиальные коэффициенты C(n, k)
from math import comb
combinations = comb(5, 2)  # 10

# Ручная реализация (стабильная)
def binomial(n, k):
    if k > n - k:  # C(n,k) = C(n,n-k)
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

# Треугольник Паскаля
def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

# Размещения A(n, k) = n!/(n-k)!
from math import perm
arrangements = perm(5, 2)  # 20

# Перестановки P(n) = n!
from itertools import permutations
perms = list(permutations([1, 2, 3]))  # 6 перестановок
```

### Полезные формулы

```python
# Сумма арифметической прогрессии
# 1 + 2 + ... + n = n(n+1)/2
sum_n = n * (n + 1) // 2

# Сумма квадратов
# 1² + 2² + ... + n² = n(n+1)(2n+1)/6
sum_squares = n * (n + 1) * (2 * n + 1) // 6

# Сумма кубов
# 1³ + 2³ + ... + n³ = (n(n+1)/2)²
sum_cubes = (n * (n + 1) // 2) ** 2

# Числа Фибоначчи (O(n))
def fibonacci(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Числа Каталана
# C_n = C(2n, n) / (n+1)
def catalan(n):
    return comb(2*n, n) // (n + 1)
```

---

## 🎯 Жадные алгоритмы

### Основные паттерны

#### 1. Сортировка + жадный выбор

```python
# Интервалы: сортируем по концу
intervals.sort(key=lambda x: x[1])

# Задачи: сортируем по дедлайну
tasks.sort(key=lambda x: x.deadline)

# Предметы: сортируем по value/weight
items.sort(key=lambda x: x.value / x.weight, reverse=True)
```

#### 2. Отслеживание максимума/минимума

```python
# Jump Game
max_reach = 0
for i in range(len(nums)):
    if i > max_reach:
        return False
    max_reach = max(max_reach, i + nums[i])

# Best Time to Buy and Sell Stock
min_price = float('inf')
max_profit = 0
for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)
```

#### 3. Два указателя

```python
# Assign Cookies
children.sort()
cookies.sort()

i = j = 0
while i < len(children) and j < len(cookies):
    if cookies[j] >= children[i]:
        i += 1  # ребёнок доволен
    j += 1  # следующее печенье

return i  # количество довольных детей
```

#### 4. Приоритетная очередь (heap)

```python
import heapq

# Для max-heap в Python используем отрицательные значения
max_heap = []
heapq.heappush(max_heap, -value)
max_val = -heapq.heappop(max_heap)

# Min-heap (по умолчанию)
min_heap = []
heapq.heappush(min_heap, value)
min_val = heapq.heappop(min_heap)

# Заправки (максимизируем топливо)
heap = []
for pos, fuel in stations:
    if pos <= max_reach:
        heapq.heappush(heap, -fuel)  # max-heap
```

### Классические жадные задачи

#### Activity Selection (расписание)

```python
def max_activities(activities):
    """
    Выбрать максимум непересекающихся активностей
    """
    # Сортируем по времени окончания
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_end = activities[0][1]

    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected
```

#### Fractional Knapsack (дробный рюкзак)

```python
def fractional_knapsack(items, capacity):
    """
    items = [(weight, value), ...]
    Можно брать дробные части
    """
    # Сортируем по value/weight (убывание)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    for weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value
```

#### Huffman Coding (сжатие)

```python
import heapq

def huffman_codes(freq):
    """
    freq = {'a': 5, 'b': 9, 'c': 12, ...}
    """
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
```

### Шаблон решения жадной задачи

```python
def greedy_solution(items):
    """
    1. Сортируем по критерию
    2. Жадно выбираем элементы
    3. Проверяем ограничения
    """
    # Шаг 1: Определяем критерий сортировки
    items.sort(key=lambda x: greedy_criterion(x))

    # Шаг 2: Инициализируем результат
    result = []
    current_state = initial_state()

    # Шаг 3: Жадно выбираем
    for item in items:
        if can_take(item, current_state):
            result.append(item)
            current_state = update_state(current_state, item)

    return result
```

---

## 📊 Таблицы сложности

### Математические операции

| Операция | Сложность | Примечание |
|----------|-----------|------------|
| НОД (Евклид) | O(log(min(a,b))) | Быстро даже для больших чисел |
| НОК | O(log(min(a,b))) | Через НОД |
| Простота числа (до √n) | O(√n) | Проверка делителей |
| Решето Эратосфена | O(n log log n) | Все простые до n |
| Разложение на множители | O(√n) | Перебор до √n |
| Факториал | O(n) | Итеративно |
| C(n,k) биномиальный | O(k) | Стабильная формула |
| Быстрое возведение | O(log n) | Битовый метод |
| Модульное возведение | O(log n) | С модулем |

### Жадные алгоритмы

| Задача | Сложность | Ключ |
|--------|-----------|------|
| Activity Selection | O(n log n) | Сортировка по концу |
| Fractional Knapsack | O(n log n) | Сортировка по value/weight |
| Huffman Coding | O(n log n) | Приоритетная очередь |
| Jump Game | O(n) | Отслеживание max_reach |
| Gas Station | O(n) | Один проход |
| Non-overlapping Intervals | O(n log n) | Activity Selection |
| Candy Distribution | O(n) | Два прохода |

---

## 🎨 Типичные паттерны кода

### Проверка всех делителей

```python
def get_divisors(n):
    """O(√n)"""
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)
```

### Битовые операции для степеней 2

```python
# Проверка степени 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Количество единичных битов
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Или просто:
bin(n).count('1')
```

### Работа с цифрами

```python
# Сумма цифр
def digit_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

# Или:
sum(int(d) for d in str(n))

# Переворот числа
def reverse_number(n):
    result = 0
    while n:
        result = result * 10 + n % 10
        n //= 10
    return result
```

---

## ⚠️ Типичные ошибки

### Математика

❌ **Деление с остатком в Python 3**
```python
# НЕПРАВИЛЬНО (в Python 3 / даёт float)
result = a / b

# ПРАВИЛЬНО (целочисленное деление)
result = a // b
```

❌ **Переполнение при умножении**
```python
# НЕПРАВИЛЬНО (может переполниться)
lcm = a * b // gcd(a, b)

# ПРАВИЛЬНО (сначала делим)
lcm = a // gcd(a, b) * b
```

❌ **Модуль отрицательного числа**
```python
# НЕПРАВИЛЬНО
result = (a - b) % MOD  # может быть отрицательным

# ПРАВИЛЬНО
result = (a - b + MOD) % MOD
```

❌ **Факториал больших чисел**
```python
# НЕПРАВИЛЬНО (медленно и большие числа)
fact = math.factorial(100000)

# ПРАВИЛЬНО (с модулем)
def factorial_mod(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result
```

### Жадные алгоритмы

❌ **Забыть отсортировать**
```python
# НЕПРАВИЛЬНО
for item in items:
    # жадный выбор

# ПРАВИЛЬНО
items.sort(key=...)
for item in items:
    # жадный выбор
```

❌ **Неправильный критерий сортировки**
```python
# Интервалы: сортировать по КОНЦУ, не по началу
intervals.sort(key=lambda x: x[1])  # ✓
intervals.sort(key=lambda x: x[0])  # ✗
```

❌ **0/1 Knapsack жадным способом**
```python
# НЕПРАВИЛЬНО (жадный НЕ работает для 0/1 knapsack)
items.sort(key=lambda x: x.value / x.weight, reverse=True)
# Нужно DP!

# ПРАВИЛЬНО только для ДРОБНОГО рюкзака
```

---

## 🔧 Полезные импорты

```python
# Математика
import math
from math import gcd, lcm, factorial, comb, perm
from functools import reduce

# Приоритетная очередь
import heapq

# Комбинаторика
from itertools import permutations, combinations, combinations_with_replacement

# Работа с дробями
from fractions import Fraction

# Decimal для точных вычислений
from decimal import Decimal, getcontext
getcontext().prec = 50  # точность 50 знаков
```

---

## 📝 Чеклист перед решением

### Математика

- [ ] Нужен ли НОД/НОК?
- [ ] Есть ли простые числа в задаче?
- [ ] Нужно ли быстрое возведение в степень?
- [ ] Есть ли модуль? (10^9+7)
- [ ] Может быть переполнение?
- [ ] Нужна ли комбинаторика?

### Greedy

- [ ] Можно ли отсортировать?
- [ ] По какому критерию сортировать?
- [ ] Можно ли доказать корректность жадного выбора?
- [ ] Не перепутал ли 0/1 knapsack с дробным?
- [ ] Нужна ли приоритетная очередь?
- [ ] Есть ли особые случаи (пустой массив, один элемент)?

---

## 💡 Советы

**Математика:**
1. Используйте `math.gcd()` вместо своей реализации
2. Для больших чисел всегда применяйте модуль
3. Решето Эратосфена - до 10^7, факторизация - до 10^12
4. Битовые операции быстрее для степеней 2

**Greedy:**
1. Сначала докажите корректность, потом кодите
2. Сортировка - друг жадных алгоритмов
3. Не все задачи решаются жадно (0/1 knapsack - DP)
4. Если жадный не работает - попробуйте DP

**Отладка:**
1. Проверьте на маленьких примерах
2. Проверьте граничные случаи (0, 1, максимум)
3. Для greedy - проверьте контрпример
4. Для math - проверьте переполнение

---

Держите эту шпаргалку под рукой при решении задач! 🚀
