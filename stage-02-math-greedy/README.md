# Этап 2: Математика и жадные алгоритмы

## Обзор

На этом этапе вы изучите базовую математику для соревнований и научитесь решать задачи жадными алгоритмами. Эти навыки критически важны для ACM!

**Время прохождения:** 2-3 недели
**Сложность:** Начальный/Средний уровень
**Требования:** Завершить Этап 1

---

## 2.1 Базовая математика для соревнований

### НОД и НОК (Наибольший общий делитель и Наименьшее общее кратное)

**НОД (GCD)** - наибольший делитель, который делит оба числа.
**НОК (LCM)** - наименьшее число, которое делится на оба числа.

#### Алгоритм Евклида для НОД

```python
def gcd(a, b):
    """
    Наибольший общий делитель (НОД)
    Алгоритм Евклида - очень быстрый O(log min(a,b))
    """
    while b:
        a, b = b, a % b
    return a

# Примеры
print(gcd(48, 18))  # 6
print(gcd(100, 35))  # 5
```

**Как это работает:**
- НОД(48, 18) = НОД(18, 12) = НОД(12, 6) = НОД(6, 0) = 6
- Каждый раз заменяем большее число остатком от деления

#### НОК через НОД

```python
def lcm(a, b):
    """
    Наименьшее общее кратное (НОК)
    Формула: LCM(a,b) = (a * b) / GCD(a,b)
    """
    return (a * b) // gcd(a, b)

# Примеры
print(lcm(12, 18))  # 36
print(lcm(5, 7))    # 35
```

#### В Python 3.9+ есть встроенные функции

```python
import math

print(math.gcd(48, 18))   # 6
print(math.lcm(12, 18))   # 36

# Для нескольких чисел
from functools import reduce
numbers = [12, 18, 24]
result = reduce(math.gcd, numbers)
print(result)  # 6
```

### Простые числа

**Простое число** - число больше 1, которое делится только на 1 и само себя.

#### Проверка на простоту (наивный способ)

```python
def is_prime_simple(n):
    """
    Простая проверка на простоту
    Время: O(n)
    """
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
```

#### Оптимизированная проверка

```python
def is_prime(n):
    """
    Оптимизированная проверка
    Время: O(√n)
    Достаточно проверить делители до √n
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Проверяем нечетные делители до √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

# Примеры
print(is_prime(17))   # True
print(is_prime(18))   # False
print(is_prime(97))   # True
```

#### Решето Эратосфена (все простые до N)

```python
def sieve_of_eratosthenes(n):
    """
    Найти все простые числа до n
    Время: O(n log log n)
    Очень быстро для n до 10^7
    """
    if n < 2:
        return []

    # Изначально все числа - потенциально простые
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Вычеркиваем составные числа
    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Вычеркиваем все кратные p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Собираем все простые
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes

# Пример
primes = sieve_of_eratosthenes(30)
print(f"Простые до 30: {primes}")
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Модульная арифметика

В соревнованиях часто просят ответ по модулю большого числа (обычно 10^9 + 7).

```python
MOD = 10**9 + 7

# Сложение по модулю
a = 123456789
b = 987654321
result = (a + b) % MOD

# Умножение по модулю
result = (a * b) % MOD

# Вычитание по модулю (важно!)
result = (a - b + MOD) % MOD  # +MOD чтобы избежать отрицательных

# Для больших произведений
def multiply_mod(a, b, mod):
    """Безопасное умножение по модулю"""
    return ((a % mod) * (b % mod)) % mod
```

### Быстрое возведение в степень

Обычное возведение в степень `a^n` работает за O(n). Быстрое - за O(log n)!

```python
def fast_power(base, exp, mod=None):
    """
    Быстрое возведение в степень
    Время: O(log exp)

    Идея: a^8 = (a^4)^2 = ((a^2)^2)^2
    """
    result = 1

    while exp > 0:
        # Если степень нечетная
        if exp % 2 == 1:
            result *= base
            if mod:
                result %= mod

        # Возводим основание в квадрат
        base *= base
        if mod:
            base %= mod

        # Делим степень пополам
        exp //= 2

    return result

# Примеры
print(fast_power(2, 10))        # 1024
print(fast_power(2, 100, MOD))  # 2^100 mod (10^9+7)
print(fast_power(5, 17, MOD))   # 5^17 mod (10^9+7)
```

**В Python 3 есть встроенная функция:**
```python
pow(2, 10, MOD)  # быстрое возведение в степень по модулю
```

### Факториалы и комбинаторика

```python
# Факториал
def factorial(n):
    """n! = 1 × 2 × 3 × ... × n"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Или используйте встроенную
import math
print(math.factorial(5))  # 120

# Факториал по модулю (для больших n)
def factorial_mod(n, mod):
    """Факториал по модулю"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

# Биномиальный коэффициент C(n, k) = n! / (k! × (n-k)!)
def binomial(n, k):
    """
    Количество способов выбрать k элементов из n
    C(n,k) = n! / (k! × (n-k)!)
    """
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1

    # Оптимизация: C(n,k) = C(n, n-k)
    k = min(k, n - k)

    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)

    return result

# Примеры
print(binomial(5, 2))  # 10 способов выбрать 2 из 5
print(binomial(10, 3))  # 120
```

### Разложение на простые множители

```python
def prime_factors(n):
    """
    Найти все простые делители числа
    Вернуть список пар (простой делитель, степень)
    """
    factors = []
    d = 2

    while d * d <= n:
        count = 0
        while n % d == 0:
            count += 1
            n //= d

        if count > 0:
            factors.append((d, count))

        d += 1

    # Если осталось число > 1, оно простое
    if n > 1:
        factors.append((n, 1))

    return factors

# Примеры
print(prime_factors(60))   # [(2, 2), (3, 1), (5, 1)] → 60 = 2² × 3 × 5
print(prime_factors(100))  # [(2, 2), (5, 2)] → 100 = 2² × 5²
```

---

## 2.2 Жадные алгоритмы (Greedy Algorithms)

**Жадный алгоритм** - на каждом шаге выбираем локально оптимальное решение в надежде получить глобальный оптимум.

### Когда работает жадный подход?

Жадный алгоритм дает правильный ответ, если задача обладает **свойством жадного выбора**:
- Локально оптимальный выбор ведет к глобальному оптимуму
- Можно доказать корректность

### Классические жадные задачи

#### 1. Задача о расписании (Activity Selection)

**Условие:** Даны N занятий с временем начала и конца. Выбрать максимальное количество непересекающихся занятий.

**Жадная стратегия:** Выбираем занятие с самым ранним временем окончания.

```python
def max_activities(activities):
    """
    activities = [(start, end), ...]
    Выбрать максимум непересекающихся активностей
    """
    # Сортируем по времени окончания
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_end = activities[0][1]

    for start, end in activities[1:]:
        # Если не пересекается с последним выбранным
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected

# Пример
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
result = max_activities(activities)
print(f"Максимум активностей: {len(result)}")
print(f"Выбранные: {result}")
```

**Почему это работает?**
- Чем раньше освобождаемся, тем больше времени для других занятий
- Выбор активности с ранним окончанием не ухудшает решение

#### 2. Задача о рюкзаке (дробный)

**Условие:** Есть рюкзак вместимости W и N предметов с весом и ценностью. Можно брать **дробные** части предметов. Максимизировать ценность.

**Жадная стратегия:** Брать предметы с наибольшей ценностью на единицу веса.

```python
def fractional_knapsack(items, capacity):
    """
    items = [(weight, value), ...]
    capacity = вместимость рюкзака
    Вернуть максимальную ценность
    """
    # Сортируем по ценности на единицу веса (убывание)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for weight, value in items:
        if remaining_capacity >= weight:
            # Берем весь предмет
            total_value += value
            remaining_capacity -= weight
        else:
            # Берем часть предмета
            fraction = remaining_capacity / weight
            total_value += value * fraction
            break

    return total_value

# Пример
items = [(10, 60), (20, 100), (30, 120)]  # (вес, ценность)
capacity = 50

result = fractional_knapsack(items, capacity)
print(f"Максимальная ценность: {result}")
```

**Важно:** Для **целочисленного** рюкзака (0/1 knapsack) жадный подход **НЕ** работает! Нужно динамическое программирование.

#### 3. Задача о монетах (сдача)

**Условие:** Выдать сдачу N монетами минимального количества. Есть монеты определенных номиналов.

**Жадная стратегия:** Берем максимально возможное количество самых крупных монет.

```python
def min_coins(amount, coins):
    """
    Выдать сдачу минимальным числом монет
    РАБОТАЕТ для "канонических" систем (1, 5, 10, 25, ...)
    """
    coins.sort(reverse=True)  # от большего к меньшему

    count = 0
    result = []

    for coin in coins:
        num_coins = amount // coin
        if num_coins > 0:
            count += num_coins
            result.extend([coin] * num_coins)
            amount -= coin * num_coins

        if amount == 0:
            break

    return count, result

# Пример
coins = [1, 5, 10, 25]
amount = 63

count, used = min_coins(amount, coins)
print(f"Сдача {amount}: {count} монет")
print(f"Монеты: {used}")
```

**Внимание:** Жадный подход работает НЕ для всех систем монет!
- Работает: [1, 5, 10, 25] (стандартные монеты)
- Не работает: [1, 3, 4] для amount=6 (жадный: 4+1+1=3 монеты, оптимум: 3+3=2 монеты)

#### 4. Задача о прыжках (Jump Game)

**Условие:** Массив чисел, где каждое число - максимальная длина прыжка с этой позиции. Можно ли дойти до конца?

**Жадная стратегия:** Отслеживаем максимально достижимую позицию.

```python
def can_jump(nums):
    """
    Проверить, можно ли дойти до последнего индекса
    """
    max_reach = 0

    for i in range(len(nums)):
        # Если текущая позиция недостижима
        if i > max_reach:
            return False

        # Обновляем максимальную достижимую позицию
        max_reach = max(max_reach, i + nums[i])

        # Если уже можем дойти до конца
        if max_reach >= len(nums) - 1:
            return True

    return False

# Примеры
print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False (застрянем на 0)
```

#### 5. Задача о заправках

**Условие:** Нужно проехать расстояние D. Бак вмещает C литров. Даны заправки на разных позициях. Минимизировать количество остановок.

**Жадная стратегия:** Едем как можно дальше, заправляемся только когда необходимо.

```python
def min_refueling_stops(target, start_fuel, stations):
    """
    target = расстояние до цели
    start_fuel = начальное топливо
    stations = [(position, fuel), ...] - заправки
    Вернуть минимальное количество остановок
    """
    import heapq

    # Используем max-heap (в Python - min-heap с отрицательными значениями)
    max_heap = []
    stops = 0
    max_reach = start_fuel
    i = 0

    while max_reach < target:
        # Добавляем все достижимые заправки в heap
        while i < len(stations) and stations[i][0] <= max_reach:
            heapq.heappush(max_heap, -stations[i][1])  # отрицательное для max-heap
            i += 1

        # Если нет доступных заправок
        if not max_heap:
            return -1

        # Берем заправку с максимальным топливом
        max_fuel = -heapq.heappop(max_heap)
        max_reach += max_fuel
        stops += 1

    return stops

# Пример
target = 100
start_fuel = 10
stations = [(10, 60), (20, 30), (30, 30), (60, 40)]
# stations.sort()  # если не отсортированы

result = min_refueling_stops(target, start_fuel, stations)
print(f"Минимум остановок: {result}")
```

### Как доказать корректность жадного алгоритма?

1. **Метод обмена (Exchange Argument)**
   - Покажите, что можно заменить элемент оптимального решения на жадный выбор без ухудшения

2. **Метод "остаться впереди" (Staying Ahead)**
   - Покажите, что жадное решение не хуже оптимального на каждом шаге

3. **Структурная индукция**
   - Докажите для базового случая и покажите, что жадный выбор сохраняет свойство

---

## Практические задачи

### Математика

1. **НОД и НОК** - найти НОД массива чисел
2. **Простые числа** - подсчитать простые числа до N (LeetCode #204)
3. **Факториалы** - вычислить C(n, k) для больших n
4. **Степень** - вычислить a^b mod M (LeetCode #50)

### Жадные алгоритмы

1. **Activity Selection** - максимум непересекающихся интервалов (LeetCode #435)
2. **Jump Game** - можно ли дойти до конца (LeetCode #55)
3. **Gas Station** - где начать путь по кольцу заправок (LeetCode #134)
4. **Candy** - раздать конфеты по правилам с минимумом конфет (LeetCode #135)

### Codeforces

- **Сложность 900-1100:** Математические задачи с жадным подходом
- Фильтр: tags включают "greedy" или "math"

---

## Следующие шаги

После освоения:
1. Решите 10-15 задач по математике
2. Решите 10-15 задач с жадными алгоритмами
3. Научитесь различать, когда жадный подход работает, а когда нужен DP
4. Переходите к **Этапу 3: Рекурсия и перебор**

Примеры кода находятся в папке `examples/`.
