"""
Простые числа и решето Эратосфена

Простое число - число > 1, которое делится только на 1 и себя
Примеры: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
"""

import time

# ============================================
# Проверка на простоту
# ============================================
print("=== ПРОВЕРКА НА ПРОСТОТУ ===\n")

def is_prime_simple(n):
    """
    Простая проверка (медленная)
    Время: O(n)
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n):
    """
    Оптимизированная проверка
    Время: O(√n)
    Достаточно проверить до √n
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Проверяем только нечетные делители до √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

# Сравнение скорости
test_number = 104729  # простое число

start = time.time()
result1 = is_prime_simple(test_number)
time1 = time.time() - start

start = time.time()
result2 = is_prime_optimized(test_number)
time2 = time.time() - start

print(f"Число: {test_number}")
print(f"Простое? {result2}")
print(f"\nПростой метод: {time1:.6f}с")
print(f"Оптимизированный: {time2:.6f}с")
print(f"Ускорение в {time1/time2:.1f} раз!")

# ============================================
# Решето Эратосфена
# ============================================
print("\n\n=== РЕШЕТО ЭРАТОСФЕНА ===")
print("Найти ВСЕ простые числа до N\n")

def sieve_of_eratosthenes(n):
    """
    Решето Эратосфена
    Время: O(n log log n) - очень быстро!
    Память: O(n)
    """
    if n < 2:
        return []

    # Сначала все числа считаем простыми
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Вычеркиваем все кратные p (начиная с p²)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Собираем все простые
    return [i for i in range(n + 1) if is_prime[i]]

# Пример
n = 50
primes = sieve_of_eratosthenes(n)
print(f"Простые числа до {n}:")
print(primes)
print(f"Всего: {len(primes)} простых чисел")

# Большой пример
n = 1000000
start = time.time()
primes = sieve_of_eratosthenes(n)
elapsed = time.time() - start

print(f"\nПростые до {n:,}: {len(primes):,} чисел")
print(f"Время: {elapsed:.3f}с")
print(f"Последние 10: {primes[-10:]}")

# ============================================
# Модифицированное решето
# ============================================
print("\n\n=== МОДИФИЦИРОВАННОЕ РЕШЕТО ===")
print("Только количество, без списка (экономия памяти)\n")

def count_primes(n):
    """Подсчитать количество простых до n"""
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False

    return sum(is_prime)

print(f"Простых до 100: {count_primes(100)}")
print(f"Простых до 1000: {count_primes(1000)}")
print(f"Простых до 10000: {count_primes(10000)}")

# ============================================
# Разложение на простые множители
# ============================================
print("\n\n=== РАЗЛОЖЕНИЕ НА ПРОСТЫЕ МНОЖИТЕЛИ ===\n")

def prime_factorization(n):
    """
    Разложить число на простые множители
    Возвращает список пар (делитель, степень)
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

def factors_to_string(factors):
    """Красиво показать разложение"""
    parts = []
    for prime, power in factors:
        if power == 1:
            parts.append(str(prime))
        else:
            parts.append(f"{prime}^{power}")
    return " × ".join(parts)

# Примеры
numbers = [60, 100, 144, 1024, 2310]
for num in numbers:
    factors = prime_factorization(num)
    print(f"{num} = {factors_to_string(factors)}")
    print(f"  Делители: {factors}")

# ============================================
# Практические задачи
# ============================================
print("\n\n=== ПРАКТИЧЕСКИЕ ЗАДАЧИ ===\n")

# Задача 1: Найти все делители числа
def all_divisors(n):
    """
    Найти все делители числа
    Используем разложение на простые множители
    """
    factors = prime_factorization(n)

    # Генерируем все делители
    divisors = [1]

    for prime, power in factors:
        new_divisors = []
        for d in divisors:
            for p in range(power + 1):
                new_divisors.append(d * (prime ** p))
        divisors = new_divisors

    return sorted(set(divisors))

print("Задача 1: Все делители числа")
n = 60
divs = all_divisors(n)
print(f"Делители {n}: {divs}")
print(f"Количество: {len(divs)}")

# Задача 2: Количество делителей
def count_divisors(n):
    """
    Количество делителей числа
    Формула: если n = p1^a1 × p2^a2 × ... × pk^ak
    то количество делителей = (a1+1) × (a2+1) × ... × (ak+1)
    """
    factors = prime_factorization(n)
    count = 1
    for prime, power in factors:
        count *= (power + 1)
    return count

print("\nЗадача 2: Количество делителей")
for n in [12, 60, 100]:
    print(f"{n} имеет {count_divisors(n)} делителей")

# Задача 3: Сумма делителей
def sum_divisors(n):
    """
    Сумма всех делителей
    Формула: если n = p^a, то сумма = (p^(a+1) - 1) / (p - 1)
    """
    factors = prime_factorization(n)
    total = 1

    for prime, power in factors:
        # Сумма 1 + p + p^2 + ... + p^a
        sum_of_powers = (prime ** (power + 1) - 1) // (prime - 1)
        total *= sum_of_powers

    return total

print("\nЗадача 3: Сумма делителей")
n = 28
s = sum_divisors(n)
print(f"Делители {n}: {all_divisors(n)}")
print(f"Сумма: {s}")
print(f"Совершенное число? {s - n == n}")  # 28 - совершенное число!

# Задача 4: N-ое простое число
def nth_prime(n):
    """Найти N-ое простое число"""
    # Оценка: n-ое простое примерно n × ln(n)
    limit = max(20, int(n * 15))  # грубая оценка

    while True:
        primes = sieve_of_eratosthenes(limit)
        if len(primes) >= n:
            return primes[n - 1]
        limit *= 2

print("\nЗадача 4: N-ое простое число")
for n in [1, 10, 100, 1000]:
    print(f"{n}-ое простое: {nth_prime(n)}")

# Задача 5: Простые числа в диапазоне
def primes_in_range(left, right):
    """Простые числа в диапазоне [left, right]"""
    if right < 2:
        return []

    # Генерируем все простые до right
    all_primes = sieve_of_eratosthenes(right)

    # Фильтруем по диапазону
    return [p for p in all_primes if p >= left]

print("\nЗадача 5: Простые в диапазоне")
left, right = 50, 100
primes = primes_in_range(left, right)
print(f"Простые от {left} до {right}: {primes}")
print(f"Количество: {len(primes)}")

# Задача 6: Близнецы (twin primes)
def find_twin_primes(n):
    """
    Простые-близнецы - пары простых чисел, различающихся на 2
    Примеры: (3,5), (5,7), (11,13), (17,19)
    """
    primes = sieve_of_eratosthenes(n)
    twins = []

    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twins.append((primes[i], primes[i + 1]))

    return twins

print("\nЗадача 6: Простые-близнецы")
twins = find_twin_primes(100)
print(f"Близнецы до 100:")
for pair in twins:
    print(f"  {pair}")

# Задача 7: Проверка числа Мерсенна
def is_mersenne_prime(p):
    """
    Число Мерсенна: M_p = 2^p - 1
    Если M_p простое и p простое, то M_p - простое число Мерсенна
    """
    if not is_prime_optimized(p):
        return False

    mersenne = 2 ** p - 1
    return is_prime_optimized(mersenne)

print("\nЗадача 7: Простые числа Мерсенна")
print("Проверяем 2^p - 1 для простых p:")
for p in [2, 3, 5, 7, 11, 13, 17, 19]:
    mersenne = 2**p - 1
    is_prime = is_mersenne_prime(p)
    print(f"  p={p}: 2^{p}-1 = {mersenne} → {'простое' if is_prime else 'составное'}")

print("\n=== Конец примеров ===")
