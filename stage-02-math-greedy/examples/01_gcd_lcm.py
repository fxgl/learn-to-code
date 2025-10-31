"""
НОД и НОК - важнейшие операции в соревновательном программировании

НОД (GCD) - Greatest Common Divisor - наибольший общий делитель
НОК (LCM) - Least Common Multiple - наименьшее общее кратное
"""

import math
from functools import reduce

# ============================================
# НОД (GCD) - Алгоритм Евклида
# ============================================
print("=== НОД (GCD) ===\n")

def gcd_iterative(a, b):
    """
    Алгоритм Евклида (итеративный)
    Время: O(log min(a,b))
    """
    print(f"Ищем НОД({a}, {b}):")
    while b:
        print(f"  {a} mod {b} = {a % b}")
        a, b = b, a % b
    print(f"Ответ: {a}\n")
    return a

# Пример 1
result = gcd_iterative(48, 18)

# Пример 2
result = gcd_iterative(100, 35)

# Рекурсивная версия (короче, но может быть медленнее для очень больших чисел)
def gcd_recursive(a, b):
    """Рекурсивная версия"""
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

print("Рекурсивная версия:")
print(f"НОД(48, 18) = {gcd_recursive(48, 18)}")

# Встроенная функция в Python (самая быстрая!)
print(f"\nВстроенная math.gcd(48, 18) = {math.gcd(48, 18)}")

# ============================================
# НОД для нескольких чисел
# ============================================
print("\n=== НОД нескольких чисел ===\n")

def gcd_multiple(numbers):
    """
    НОД для списка чисел
    Свойство: НОД(a, b, c) = НОД(НОД(a, b), c)
    """
    return reduce(math.gcd, numbers)

numbers = [12, 18, 24, 30]
result = gcd_multiple(numbers)
print(f"Числа: {numbers}")
print(f"НОД всех чисел: {result}")

# ============================================
# НОК (LCM)
# ============================================
print("\n\n=== НОК (LCM) ===\n")

def lcm(a, b):
    """
    Наименьшее общее кратное
    Формула: НОК(a,b) = (a × b) / НОД(a,b)
    """
    return (a * b) // math.gcd(a, b)

print(f"НОК(12, 18) = {lcm(12, 18)}")
print(f"Проверка: 36 делится на 12? {36 % 12 == 0}")
print(f"Проверка: 36 делится на 18? {36 % 18 == 0}")

# В Python 3.9+ есть встроенная функция
if hasattr(math, 'lcm'):
    print(f"\nВстроенная math.lcm(12, 18) = {math.lcm(12, 18)}")

# НОК для нескольких чисел
def lcm_multiple(numbers):
    """НОК для списка чисел"""
    if hasattr(math, 'lcm'):
        return reduce(math.lcm, numbers)
    else:
        return reduce(lcm, numbers)

numbers = [4, 6, 8]
result = lcm_multiple(numbers)
print(f"\nЧисла: {numbers}")
print(f"НОК всех чисел: {result}")

# ============================================
# Практические задачи
# ============================================
print("\n\n=== ПРАКТИЧЕСКИЕ ЗАДАЧИ ===\n")

# Задача 1: Упростить дробь
def simplify_fraction(numerator, denominator):
    """Упростить дробь до несократимого вида"""
    g = math.gcd(numerator, denominator)
    return numerator // g, denominator // g

print("Задача 1: Упростить дробь")
num, den = simplify_fraction(48, 18)
print(f"48/18 = {num}/{den}")

num, den = simplify_fraction(100, 35)
print(f"100/35 = {num}/{den}")

# Задача 2: Когда встретятся две лампочки?
def when_lights_meet(period1, period2):
    """
    Две лампочки мигают с периодами period1 и period2 секунд.
    Через сколько секунд они мигнут одновременно?

    Ответ: НОК периодов
    """
    return lcm(period1, period2)

print("\nЗадача 2: Когда лампочки мигнут вместе?")
period1, period2 = 6, 8
result = when_lights_meet(period1, period2)
print(f"Периоды: {period1}с и {period2}с")
print(f"Мигнут вместе через: {result}с")

# Задача 3: Разделить шоколадку
def divide_chocolate(rows, cols):
    """
    Есть шоколадка rows×cols.
    На сколько одинаковых квадратных кусочков максимального размера можно разделить?

    Размер кусочка: НОД(rows, cols)
    Количество: (rows × cols) / (НОД² )
    """
    piece_size = math.gcd(rows, cols)
    num_pieces = (rows * cols) // (piece_size * piece_size)
    return piece_size, num_pieces

print("\nЗадача 3: Разделить шоколадку")
rows, cols = 12, 8
size, count = divide_chocolate(rows, cols)
print(f"Шоколадка: {rows}×{cols}")
print(f"Максимальный размер квадрата: {size}×{size}")
print(f"Количество кусочков: {count}")

# Задача 4: Расстановка деревьев
def trees_on_road(length):
    """
    На дороге длины length метров нужно посадить деревья
    через равные расстояния (в целых метрах).
    Сколько максимум деревьев можно посадить?

    Если расстояние = d, то деревьев = length/d + 1
    Минимальное d (максимум деревьев) - это делители length
    """
    # Найдем все делители
    divisors = []
    for i in range(1, int(length**0.5) + 1):
        if length % i == 0:
            divisors.append(i)
            if i != length // i:
                divisors.append(length // i)

    divisors.sort()
    print(f"Делители {length}: {divisors}")

    # Деревья для каждого расстояния
    for d in divisors[:5]:  # показываем первые 5
        trees = length // d + 1
        print(f"  Расстояние {d}м → {trees} деревьев")

print("\nЗадача 4: Деревья на дороге")
trees_on_road(24)

# Задача 5: НОД массива
def gcd_array(arr):
    """Найти НОД всех элементов массива"""
    return reduce(math.gcd, arr)

print("\nЗадача 5: НОД массива")
arr = [12, 18, 24, 30, 36]
result = gcd_array(arr)
print(f"Массив: {arr}")
print(f"НОД всех элементов: {result}")

# Задача 6: Проверка на взаимно простые
def are_coprime(a, b):
    """
    Взаимно простые числа - числа, НОД которых равен 1
    (не имеют общих делителей кроме 1)
    """
    return math.gcd(a, b) == 1

print("\nЗадача 6: Взаимно простые числа")
pairs = [(8, 9), (12, 18), (7, 15), (10, 21)]
for a, b in pairs:
    coprime = are_coprime(a, b)
    print(f"НОД({a}, {b}) = {math.gcd(a, b)} → "
          f"{'взаимно простые' if coprime else 'не взаимно простые'}")

# ============================================
# Расширенный алгоритм Евклида
# ============================================
print("\n\n=== РАСШИРЕННЫЙ АЛГОРИТМ ЕВКЛИДА ===")
print("Находит не только НОД, но и коэффициенты x, y:")
print("НОД(a,b) = a×x + b×y\n")

def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида
    Возвращает (gcd, x, y) такие что: gcd = a×x + b×y
    """
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y

a, b = 35, 15
gcd, x, y = extended_gcd(a, b)
print(f"НОД({a}, {b}) = {gcd}")
print(f"Коэффициенты: x={x}, y={y}")
print(f"Проверка: {a}×{x} + {b}×{y} = {a*x + b*y}")

# Применение: решение линейного диофантова уравнения
print("\nПрименение: решить уравнение 35x + 15y = 5")
# Сначала проверяем, делится ли 5 на НОД(35, 15)
target = 5
if target % gcd == 0:
    k = target // gcd
    x_sol = x * k
    y_sol = y * k
    print(f"Одно из решений: x={x_sol}, y={y_sol}")
    print(f"Проверка: 35×{x_sol} + 15×{y_sol} = {35*x_sol + 15*y_sol}")
else:
    print("Решений нет (5 не делится на НОД)")

print("\n=== Конец примеров ===")
