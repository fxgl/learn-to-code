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

### Примеры задач на математику

#### Задача 1: НОД строк
**Платформа:** [LeetCode #1071 - Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | **Сложность:** Easy

**Условие:** Для двух строк найти наибольшую общую подстроку-делитель.

**Пример:**
```
Вход: str1 = "ABCABC", str2 = "ABC"
Выход: "ABC"

Вход: str1 = "ABABAB", str2 = "ABAB"
Выход: "AB"
```

**Решение:**
```python
import math

def gcd_of_strings(str1, str2):
    """
    НОД строк работает только если str1 + str2 == str2 + str1
    Длина НОД = НОД(len(str1), len(str2))
    """
    # Проверяем, что строки вообще имеют общий делитель
    if str1 + str2 != str2 + str1:
        return ""

    # Находим НОД длин
    gcd_len = math.gcd(len(str1), len(str2))

    # НОД строки - это первые gcd_len символов
    return str1[:gcd_len]

# Тесты
print(gcd_of_strings("ABCABC", "ABC"))     # "ABC"
print(gcd_of_strings("ABABAB", "ABAB"))    # "AB"
print(gcd_of_strings("LEET", "CODE"))      # ""
```

**Что здесь используется:**
- ✅ `math.gcd()` для нахождения НОД длин
- ✅ Свойство: если есть общий делитель, то str1 + str2 == str2 + str1
- ✅ Срезы строк

---

#### Задача 2: Count Primes
**Платформа:** [LeetCode #204 - Count Primes](https://leetcode.com/problems/count-primes/) | **Сложность:** Medium

**Условие:** Подсчитать количество простых чисел меньше n.

**Пример:**
```
Вход: n = 10
Выход: 4
Объяснение: 2, 3, 5, 7
```

**Решение с решетом Эратосфена:**
```python
def count_primes(n):
    """
    Решето Эратосфена
    Время: O(n log log n)
    Память: O(n)
    """
    if n < 2:
        return 0

    # Создаем массив - все изначально простые
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    # Вычеркиваем составные числа
    p = 2
    while p * p < n:
        if is_prime[p]:
            # Вычеркиваем все кратные p
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1

    # Подсчитываем простые
    return sum(is_prime)

# Тесты
print(count_primes(10))      # 4 → [2, 3, 5, 7]
print(count_primes(100))     # 25
print(count_primes(1000))    # 168
```

**Оптимизация:**
```python
def count_primes_optimized(n):
    """Оптимизированная версия - проверяем только нечетные"""
    if n < 3:
        return 0

    # Массив для нечетных чисел (3, 5, 7, ...)
    # is_prime[i] соответствует числу 2*i + 3
    is_prime = [True] * (n // 2)

    p = 3
    while p * p < n:
        if is_prime[p // 2]:
            # Вычеркиваем кратные p (только нечетные)
            for i in range(p * p, n, 2 * p):
                is_prime[i // 2] = False
        p += 2

    # +1 для числа 2
    return sum(is_prime) + 1

print(count_primes_optimized(10))   # 4
```

**Что здесь используется:**
- ✅ Решето Эратосфена
- ✅ Оптимизация: проверяем только до √n
- ✅ Оптимизация: работаем только с нечетными числами

---

#### Задача 3: Power of Three
**Платформа:** [LeetCode #326 - Power of Three](https://leetcode.com/problems/power-of-three/) | **Сложность:** Easy

**Условие:** Определить, является ли число степенью тройки.

**Пример:**
```
Вход: n = 27
Выход: True (3^3 = 27)

Вход: n = 45
Выход: False
```

**Решение 1: Деление в цикле**
```python
def is_power_of_three_loop(n):
    """Делим на 3 пока возможно"""
    if n < 1:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1

# Тесты
print(is_power_of_three_loop(27))   # True
print(is_power_of_three_loop(45))   # False
```

**Решение 2: Математический трюк**
```python
def is_power_of_three(n):
    """
    Математический трюк:
    3^19 = 1162261467 - максимальная степень 3 в int32
    Если n - степень 3, то 3^19 делится на n
    """
    return n > 0 and 1162261467 % n == 0
```

**Решение 3: Логарифмы**
```python
import math

def is_power_of_three_log(n):
    """Используем логарифмы"""
    if n < 1:
        return False

    # log₃(n) = log(n) / log(3)
    # Если n = 3^k, то log₃(n) = k (целое число)
    log_val = math.log10(n) / math.log10(3)

    # Проверяем, что это целое число
    return abs(log_val - round(log_val)) < 1e-10

print(is_power_of_three_log(27))    # True
```

**Что здесь используется:**
- ✅ Деление с остатком
- ✅ Математические свойства степеней
- ✅ Логарифмы

---

#### Задача 4: Factorial Trailing Zeroes
**Платформа:** [LeetCode #172 - Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | **Сложность:** Medium

**Условие:** Найти количество нулей в конце n!

**Пример:**
```
Вход: n = 5
Выход: 1
Объяснение: 5! = 120, один ноль в конце
```

**Наивное решение (не работает для больших n):**
```python
def trailing_zeroes_naive(n):
    """Вычислить факториал и посчитать нули - МЕДЛЕННО!"""
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    count = 0
    while factorial % 10 == 0:
        count += 1
        factorial //= 10

    return count
```

**Оптимальное решение:**
```python
def trailing_zeroes(n):
    """
    Нули образуются от множителей 10 = 2 × 5
    Двоек всегда больше, чем пятерок
    → Считаем количество пятерок в разложении n!

    Пятерки дают: 5, 10, 15, 20, 25, ...
    25 = 5² даёт две пятёрки!
    125 = 5³ даёт три пятёрки!

    Формула: n/5 + n/25 + n/125 + ...
    """
    count = 0
    power_of_5 = 5

    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5

    return count

# Тесты
print(trailing_zeroes(5))      # 1  (5! = 120)
print(trailing_zeroes(10))     # 2  (10! = 3628800)
print(trailing_zeroes(25))     # 6  (25! имеет 6 нулей)
print(trailing_zeroes(100))    # 24
```

**Объяснение:**
```python
# Для n = 25:
# 25/5 = 5    (числа: 5, 10, 15, 20, 25)
# 25/25 = 1   (число 25 = 5², дает еще одну пятерку)
# Итого: 5 + 1 = 6 нулей
```

**Что здесь используется:**
- ✅ Разложение на простые множители
- ✅ Подсчет кратных 5, 25, 125, ...
- ✅ Математическая оптимизация

---

#### Задача 5: Climbing Stairs (комбинаторика)
**Платформа:** [LeetCode #70 - Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | **Сложность:** Easy

**Условие:** Можно подниматься на 1 или 2 ступени. Сколько способов подняться на n ступеней?

**Пример:**
```
Вход: n = 3
Выход: 3
Объяснение: 1+1+1, 1+2, 2+1
```

**Решение 1: Рекурсия (медленно)**
```python
def climb_stairs_recursive(n):
    """Наивная рекурсия - O(2^n)"""
    if n <= 2:
        return n
    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)
```

**Решение 2: Числа Фибоначчи**
```python
def climb_stairs(n):
    """
    Это числа Фибоначчи!
    f(n) = f(n-1) + f(n-2)
    Время: O(n), память: O(1)
    """
    if n <= 2:
        return n

    prev, curr = 1, 2

    for i in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr

# Тесты
print(climb_stairs(3))   # 3
print(climb_stairs(4))   # 5
print(climb_stairs(5))   # 8
```

**Решение 3: Формула через комбинаторику**
```python
def climb_stairs_formula(n):
    """
    Комбинаторная формула:
    Если делаем k шагов по 2, то шагов по 1 = n - 2k
    Всего шагов = k + (n - 2k) = n - k
    Количество способов = C(n-k, k)
    """
    from math import comb

    result = 0
    k = 0
    while 2 * k <= n:
        # k шагов по 2, остальные по 1
        result += comb(n - k, k)
        k += 1

    return result

print(climb_stairs_formula(5))   # 8
```

**Что здесь используется:**
- ✅ Рекурсия → динамическое программирование
- ✅ Числа Фибоначчи
- ✅ Биномиальные коэффициенты

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

### Разобранные задачи на жадные алгоритмы

#### Задача 6: Jump Game
**Платформа:** [LeetCode #55 - Jump Game](https://leetcode.com/problems/jump-game/) | **Сложность:** Medium

**Условие:** Дан массив чисел, где каждое число показывает максимальную длину прыжка. Можно ли дойти до последнего индекса?

**Пример:**
```
Вход: nums = [2,3,1,1,4]
Выход: True
Объяснение: Прыгаем на 1 позицию, потом на 3 позиции до конца

Вход: nums = [3,2,1,0,4]
Выход: False
Объяснение: Всегда окажемся на индексе 3, где максимальный прыжок = 0
```

**Решение:**
```python
def can_jump(nums):
    """
    Жадный подход: отслеживаем максимально достижимую позицию
    Время: O(n), Память: O(1)
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

# Тесты
print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
print(can_jump([0]))              # True (уже на конечной позиции)
```

**Что здесь используется:**
- ✅ Жадный выбор: отслеживаем максимальную достижимую позицию
- ✅ Один проход по массиву
- ✅ Ранний выход при достижении цели

---

#### Задача 7: Jump Game II (минимум прыжков)
**Платформа:** [LeetCode #45 - Jump Game II](https://leetcode.com/problems/jump-game-ii/) | **Сложность:** Medium

**Условие:** Найти минимальное количество прыжков, чтобы дойти до конца массива. Гарантируется, что дойти можно.

**Пример:**
```
Вход: nums = [2,3,1,1,4]
Выход: 2
Объяснение: Прыжок на индекс 1, потом на последний индекс
```

**Решение 1: Жадный с уровнями (BFS-подход)**
```python
def jump(nums):
    """
    Представляем как BFS: каждый прыжок = новый уровень
    Время: O(n), Память: O(1)
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0      # конец текущего уровня
    farthest = 0         # самая дальняя точка, которую можем достичь

    for i in range(len(nums) - 1):
        # Обновляем самую дальнюю достижимую позицию
        farthest = max(farthest, i + nums[i])

        # Если дошли до конца текущего уровня
        if i == current_end:
            jumps += 1
            current_end = farthest

            # Если уже можем достичь конца
            if current_end >= len(nums) - 1:
                break

    return jumps

# Тесты
print(jump([2, 3, 1, 1, 4]))  # 2
print(jump([2, 3, 0, 1, 4]))  # 2
```

**Решение 2: Более интуитивный жадный**
```python
def jump_v2(nums):
    """
    Жадный: на каждом шаге прыгаем к позиции,
    с которой можем прыгнуть дальше всего
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_pos = 0

    while current_pos < len(nums) - 1:
        # Если можем сразу допрыгнуть до конца
        if current_pos + nums[current_pos] >= len(nums) - 1:
            return jumps + 1

        # Найти лучшую позицию для следующего прыжка
        max_reach = 0
        best_pos = current_pos

        for next_pos in range(current_pos + 1, current_pos + nums[current_pos] + 1):
            if next_pos + nums[next_pos] > max_reach:
                max_reach = next_pos + nums[next_pos]
                best_pos = next_pos

        current_pos = best_pos
        jumps += 1

    return jumps

print(jump_v2([2, 3, 1, 1, 4]))  # 2
```

**Что здесь используется:**
- ✅ Жадный выбор: прыгаем в позицию с максимальным "reach"
- ✅ BFS-подобный подход с уровнями
- ✅ Оптимизация: O(n) вместо O(n²)

---

#### Задача 8: Non-overlapping Intervals (расписание)
**Платформа:** [LeetCode #435 - Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | **Сложность:** Medium

**Условие:** Дан массив интервалов. Найти минимальное количество интервалов для удаления, чтобы остальные не пересекались.

**Пример:**
```
Вход: intervals = [[1,2],[2,3],[3,4],[1,3]]
Выход: 1
Объяснение: Удаляем [1,3], остальные не пересекаются
```

**Решение:**
```python
def erase_overlap_intervals(intervals):
    """
    Жадная стратегия: выбираем интервалы с ранним окончанием
    (обратная задача Activity Selection)
    Время: O(n log n), Память: O(1)
    """
    if not intervals:
        return 0

    # Сортируем по времени окончания
    intervals.sort(key=lambda x: x[1])

    removed = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        # Если интервал пересекается с предыдущим
        if start < prev_end:
            removed += 1
            # prev_end не меняем (оставляем интервал с ранним окончанием)
        else:
            # Интервал не пересекается
            prev_end = end

    return removed

# Тесты
print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))      # 1
print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))            # 2
print(erase_overlap_intervals([[1,2],[2,3]]))                  # 0
```

**Альтернативное решение (считаем максимум непересекающихся):**
```python
def erase_overlap_intervals_v2(intervals):
    """
    Сначала находим максимум непересекающихся интервалов,
    потом вычитаем из общего количества
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])

    count = 1  # первый интервал всегда берем
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= prev_end:
            count += 1
            prev_end = intervals[i][1]

    return len(intervals) - count

print(erase_overlap_intervals_v2([[1,2],[2,3],[3,4],[1,3]]))  # 1
```

**Что здесь используется:**
- ✅ Activity Selection Problem (классическая жадная задача)
- ✅ Сортировка по времени окончания
- ✅ Два подхода: прямой подсчет и через максимум

---

#### Задача 9: Gas Station (круговой маршрут)
**Платформа:** [LeetCode #134 - Gas Station](https://leetcode.com/problems/gas-station/) | **Сложность:** Medium

**Условие:** N заправок по кругу. Дано gas[i] (бензин на i-й заправке) и cost[i] (стоимость до i+1 заправки). Найти стартовую заправку, чтобы проехать полный круг. Если нет решения - вернуть -1.

**Пример:**
```
Вход: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Выход: 3
Объяснение:
Старт на станции 3:
  Бак: 0 + 4 = 4, едем до 4, -1 бензина, остаётся 3
  Бак: 3 + 5 = 8, едем до 0, -2 бензина, остаётся 6
  и т.д.
```

**Решение:**
```python
def can_complete_circuit(gas, cost):
    """
    Жадный подход с двумя наблюдениями:
    1. Если total_gas >= total_cost, решение существует
    2. Если не можем дойти от А до Б, то и с любой промежуточной
       станции между А и Б тоже не сможем

    Время: O(n), Память: O(1)
    """
    total_gas = 0
    total_cost = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        # Если бак опустел
        if tank < 0:
            # Начинаем со следующей станции
            start = i + 1
            tank = 0

    # Если суммарный бензин >= суммарные затраты
    return start if total_gas >= total_cost else -1

# Тесты
print(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))  # 3
print(can_complete_circuit([2,3,4], [3,4,3]))          # -1
print(can_complete_circuit([5,1,2,3,4], [4,4,1,5,1]))  # 4
```

**Почему это работает:**
```python
# Ключевое наблюдение:
# Если не можем доехать от станции i до станции j,
# то не сможем доехать и от любой станции между i и j до j.
#
# Доказательство от противного:
# Пусть можем доехать от k (i < k < j) до j.
# Но мы могли доехать от i до k (иначе бы start уже сменился).
# Значит, от i до j тоже могли бы доехать. Противоречие.
```

**Что здесь используется:**
- ✅ Жадный выбор стартовой позиции
- ✅ Математическое доказательство корректности
- ✅ Один проход по массиву

---

#### Задача 10: Best Time to Buy and Sell Stock II
**Платформа:** [LeetCode #122 - Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | **Сложность:** Medium

**Условие:** Дан массив цен акций. Можно совершать неограниченное количество сделок (купить-продать), но не более одной акции в руках. Максимизировать прибыль.

**Пример:**
```
Вход: prices = [7,1,5,3,6,4]
Выход: 7
Объяснение: Купить день 2 (цена 1), продать день 3 (цена 5), прибыль = 4
            Купить день 4 (цена 3), продать день 5 (цена 6), прибыль = 3
            Итого: 4 + 3 = 7
```

**Решение 1: Жадный (суммируем все возрастания)**
```python
def max_profit(prices):
    """
    Жадная стратегия: покупаем перед каждым ростом,
    продаем на пике

    Эквивалентно: суммируем все положительные разности
    Время: O(n), Память: O(1)
    """
    profit = 0

    for i in range(1, len(prices)):
        # Если цена выросла - берем эту прибыль
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

# Тесты
print(max_profit([7,1,5,3,6,4]))     # 7
print(max_profit([1,2,3,4,5]))       # 4 (каждый день растет)
print(max_profit([7,6,4,3,1]))       # 0 (только падает)
```

**Решение 2: Более явное (отслеживаем покупку/продажу)**
```python
def max_profit_explicit(prices):
    """
    Явно отслеживаем моменты покупки и продажи
    """
    profit = 0
    i = 0
    n = len(prices)

    while i < n - 1:
        # Найти локальный минимум (момент покупки)
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        buy = prices[i]

        # Найти локальный максимум (момент продажи)
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        sell = prices[i]

        profit += sell - buy

    return profit

print(max_profit_explicit([7,1,5,3,6,4]))  # 7
```

**Визуализация:**
```python
# Цены:     [7, 1, 5, 3, 6, 4]
# Разности:    -6 +4 -2 +3 -2
# Берем только положительные: 4 + 3 = 7

# Почему это работает?
# Покупка в день 1 и продажа в день 3:
# profit = prices[3] - prices[1]
#        = (prices[3] - prices[2]) + (prices[2] - prices[1])
# Это то же самое, что суммировать все возрастания!
```

**Что здесь используется:**
- ✅ Жадный выбор: берем каждое возрастание
- ✅ Математическое свойство разностей
- ✅ Локальные минимумы/максимумы

---

#### Задача 11: Candy (распределение конфет)
**Платформа:** [LeetCode #135 - Candy](https://leetcode.com/problems/candy/) | **Сложность:** Hard

**Условие:** N детей с рейтингами. Правила:
1. Каждый ребёнок получает минимум 1 конфету
2. Ребёнок с более высоким рейтингом, чем сосед, должен получить больше конфет

Найти минимальное количество конфет.

**Пример:**
```
Вход: ratings = [1,0,2]
Выход: 5
Объяснение: [2,1,2] - минимальное распределение

Вход: ratings = [1,2,2]
Выход: 4
Объяснение: [1,2,1]
```

**Решение: Два прохода**
```python
def candy(ratings):
    """
    Жадная стратегия с двумя проходами:
    1. Слева направо: учитываем левого соседа
    2. Справа налево: учитываем правого соседа

    Время: O(n), Память: O(n)
    """
    n = len(ratings)
    if n == 0:
        return 0

    candies = [1] * n  # изначально всем по 1 конфете

    # Проход слева направо
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # Проход справа налево
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)

# Тесты
print(candy([1,0,2]))           # 5: [2,1,2]
print(candy([1,2,2]))           # 4: [1,2,1]
print(candy([1,3,2,2,1]))       # 7: [1,2,1,2,1]
print(candy([1,2,87,87,87,2,1]))  # 13: [1,2,3,1,3,2,1]
```

**Объяснение:**
```python
# ratings = [1, 3, 2, 2, 1]

# После прохода слева направо:
# candies = [1, 2, 1, 1, 1]
# (учли: 1<3, остальные не больше левого соседа)

# После прохода справа налево:
# candies = [1, 2, 1, 2, 1]
# (учли: 2>1 справа, нужно минимум 2)

# Итого: 1+2+1+2+1 = 7
```

**Почему нужны ДВА прохода:**
```python
# Один проход не работает:
# ratings = [1, 2, 3, 1]

# Только слева направо:
# candies = [1, 2, 3, 1] ❌ (3 > 1, но у позиции 3 меньше конфет)

# С двумя проходами:
# Слева направо:  [1, 2, 3, 1]
# Справа налево: [1, 2, 3, 1] (позиция 2 имеет 3>1, проверяем max(3, 1+1)=3)
# Результат: [1, 2, 3, 1] = 7 ✓
```

**Что здесь используется:**
- ✅ Жадный подход с двумя проходами
- ✅ Учёт соседей с обеих сторон
- ✅ Использование max для разрешения конфликтов

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
