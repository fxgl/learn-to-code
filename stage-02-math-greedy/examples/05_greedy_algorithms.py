"""
Этап 2: Математика и жадные алгоритмы
Пример 5: Жадные алгоритмы

Запустите этот файл, чтобы увидеть примеры:
- Классических жадных задач
- Доказательства корректности
- Когда жадный подход работает и когда НЕТ

python3 05_greedy_algorithms.py
"""

print("=" * 60)
print("ЖАДНЫЕ АЛГОРИТМЫ (GREEDY)")
print("=" * 60)

# ============================================================
# 1. ЧТО ТАКОЕ ЖАДНЫЙ АЛГОРИТМ?
# ============================================================

print("\n1. ЧТО ТАКОЕ ЖАДНЫЙ АЛГОРИТМ?")
print("-" * 60)

print("""
Жадный алгоритм - на каждом шаге выбираем локально оптимальное
решение в надежде получить глобальный оптимум.

КОГДА РАБОТАЕТ:
  ✅ Задача обладает свойством жадного выбора
  ✅ Локально оптимальный выбор → глобальный оптимум
  ✅ Можно доказать корректность

КОГДА НЕ РАБОТАЕТ:
  ❌ 0/1 Knapsack (целочисленный рюкзак)
  ❌ Longest Common Subsequence
  ❌ Edit Distance
  → Для таких задач нужно динамическое программирование!
""")

# ============================================================
# 2. ACTIVITY SELECTION (Расписание)
# ============================================================

print("\n\n2. ACTIVITY SELECTION (Выбор занятий)")
print("-" * 60)

print("Задача: Выбрать максимум непересекающихся интервалов")
print("Жадная стратегия: Сортировка по времени окончания\n")


def activity_selection(activities):
    """
    Выбрать максимум непересекающихся активностей
    activities = [(start, end), ...]
    """
    if not activities:
        return []

    # КЛЮЧ: Сортируем по времени окончания!
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
activities = [
    (1, 3),   # A
    (2, 5),   # B
    (4, 6),   # C
    (6, 7),   # D
    (5, 9),   # E
    (8, 9)    # F
]

print(f"Активности: {activities}")
result = activity_selection(activities)
print(f"\nВыбранные: {result}")
print(f"Количество: {len(result)}")

print("\nВизуализация:")
print("  0  1  2  3  4  5  6  7  8  9")
print("  |--|  |     A (выбрано)")
print("     |-----|  B")
print("        |--|  C")
print("           |-|  D (выбрано)")
print("         |----|  E")
print("              |-|  F")

print("\n✅ Почему сортируем по КОНЦУ, а не по началу?")
print("  Чем раньше освобождаемся → больше времени для других")

# ============================================================
# 3. FRACTIONAL KNAPSACK (Дробный рюкзак)
# ============================================================

print("\n\n3. FRACTIONAL KNAPSACK (Дробный рюкзак)")
print("-" * 60)

print("Задача: Максимизировать ценность, можно брать дробные части")
print("Жадная стратегия: Сортировка по ценности на единицу веса\n")


def fractional_knapsack(items, capacity):
    """
    items = [(weight, value), ...]
    capacity = вместимость рюкзака
    МОЖНО брать дробные части предметов
    """
    # Сортируем по value/weight (убывание)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    details = []

    for weight, value in items:
        value_per_unit = value / weight

        if capacity >= weight:
            # Берём весь предмет
            total_value += value
            capacity -= weight
            details.append(f"Весь предмет ({weight}кг, {value}₽) → +{value}₽")
        else:
            # Берём часть предмета
            fraction = capacity / weight
            added_value = value * fraction
            total_value += added_value
            details.append(f"Часть предмета ({capacity:.1f}кг из {weight}кг) → +{added_value:.1f}₽")
            break

    return total_value, details


# Пример
items = [
    (10, 60),   # 6₽/кг
    (20, 100),  # 5₽/кг
    (30, 120)   # 4₽/кг
]
capacity = 50

print(f"Предметы (вес, ценность): {items}")
print(f"Вместимость рюкзака: {capacity} кг\n")

total, details = fractional_knapsack(items, capacity)

print("Решение:")
for step in details:
    print(f"  {step}")
print(f"\nМаксимальная ценность: {total}₽")

print("\n⚠️ ВАЖНО: Для ЦЕЛОЧИСЛЕННОГО рюкзака (0/1 Knapsack)")
print("   жадный подход НЕ работает! Нужно DP.")

# ============================================================
# 4. COIN CHANGE (Монеты для сдачи)
# ============================================================

print("\n\n4. COIN CHANGE (Выдача сдачи)")
print("-" * 60)

print("Задача: Выдать сдачу минимальным количеством монет")
print("Жадная стратегия: Берём максимально крупные монеты\n")


def greedy_coin_change(amount, coins):
    """
    РАБОТАЕТ для 'канонических' систем монет
    Например: [1, 5, 10, 25]
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


# Пример 1: Работает
coins1 = [1, 5, 10, 25]
amount1 = 63

count, used = greedy_coin_change(amount1, coins1)
print(f"Сдача {amount1}₽ монетами {coins1}:")
print(f"  Использовано: {used}")
print(f"  Количество: {count} монет")

# Пример 2: НЕ работает!
print("\n⚠️ Контрпример (жадный НЕ работает):")
coins2 = [1, 3, 4]
amount2 = 6

count_greedy, used_greedy = greedy_coin_change(amount2, coins2)
print(f"\nСдача {amount2}₽ монетами {coins2}:")
print(f"  Жадный подход: {used_greedy} = {count_greedy} монет")
print(f"  Оптимум:       [3, 3] = 2 монеты")
print(f"  ❌ Жадный дал неоптимальный ответ!")

# ============================================================
# 5. JUMP GAME (Можно ли дойти до конца)
# ============================================================

print("\n\n5. JUMP GAME (Прыжки по массиву)")
print("-" * 60)

print("Задача: nums[i] = макс прыжок с позиции i. Дойти до конца?")
print("Жадная стратегия: Отслеживаем максимально достижимую позицию\n")


def can_jump(nums):
    """
    Жадный подход: отслеживаем max_reach
    Время: O(n), Память: O(1)
    """
    max_reach = 0

    for i in range(len(nums)):
        # Если текущая позиция недостижима
        if i > max_reach:
            return False

        # Обновляем максимальную достижимую позицию
        max_reach = max(max_reach, i + nums[i])

        # Ранний выход
        if max_reach >= len(nums) - 1:
            return True

    return True


# Примеры
test_cases = [
    ([2, 3, 1, 1, 4], True, "Можем: 0→1→4"),
    ([3, 2, 1, 0, 4], False, "Застрянем на индексе 3"),
    ([0], True, "Уже на конце"),
    ([2, 0, 0], True, "Прыгаем через нули")
]

for nums, expected, explanation in test_cases:
    result = can_jump(nums)
    status = "✓" if result == expected else "✗"
    print(f"{status} {nums} → {result} ({explanation})")

# ============================================================
# 6. GAS STATION (Круговой маршрут)
# ============================================================

print("\n\n6. GAS STATION (Заправки по кругу)")
print("-" * 60)

print("Задача: Найти стартовую заправку для полного круга")
print("Жадная стратегия: Если не доехали от A до B,")
print("  то не доедем и с любой промежуточной станции\n")


def can_complete_circuit(gas, cost):
    """
    gas[i] - бензин на i-й заправке
    cost[i] - стоимость до следующей
    Вернуть индекс стартовой заправки или -1
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

    # Решение существует, если total_gas >= total_cost
    return start if total_gas >= total_cost else -1


# Пример
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

result = can_complete_circuit(gas, cost)
print(f"gas  = {gas}")
print(f"cost = {cost}")
print(f"\nСтартовая станция: {result}")

if result != -1:
    print(f"\nПроверка (старт от станции {result}):")
    tank = 0
    for i in range(len(gas)):
        station = (result + i) % len(gas)
        tank += gas[station]
        print(f"  Станция {station}: бак = {tank}, едем (-{cost[station]})")
        tank -= cost[station]
    print(f"  Финал: бак = {tank} ✓")

# ============================================================
# 7. ASSIGN COOKIES (Раздача печенек)
# ============================================================

print("\n\n7. ASSIGN COOKIES (Раздача печенек)")
print("-" * 60)

print("Задача: Максимизировать количество довольных детей")
print("Жадная стратегия: Сортируем оба массива, жадно назначаем\n")


def assign_cookies(children, cookies):
    """
    children[i] - жадность i-го ребёнка
    cookies[j] - размер j-го печенья
    Ребёнок доволен если cookies[j] >= children[i]
    """
    children.sort()
    cookies.sort()

    i = j = 0  # два указателя

    while i < len(children) and j < len(cookies):
        # Если печенье подходит
        if cookies[j] >= children[i]:
            i += 1  # ребёнок доволен, переходим к следующему
        j += 1  # переходим к следующему печенью

    return i  # количество довольных детей


# Пример
children = [1, 2, 3]
cookies = [1, 1]

result = assign_cookies(children, cookies)
print(f"Жадность детей: {children}")
print(f"Размеры печенек: {cookies}")
print(f"Довольных детей: {result}")

print("\nРешение:")
print("  Ребёнок с жадностью 1 → печенье размера 1 ✓")
print("  Ребёнок с жадностью 2 → печенье размера 1 ✗")
print("  Ребёнок с жадностью 3 → печенья нет ✗")

# ============================================================
# 8. КАК ДОКАЗАТЬ КОРРЕКТНОСТЬ?
# ============================================================

print("\n\n8. ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ")
print("-" * 60)

print("""
МЕТОД 1: Exchange Argument (Метод обмена)
  1. Пусть OPT - оптимальное решение
  2. Пусть GREEDY - жадное решение
  3. Покажите, что можно заменить элемент в OPT
     на жадный выбор без ухудшения
  4. → Жадное решение не хуже оптимального

МЕТОД 2: Staying Ahead (Остаться впереди)
  1. Покажите, что жадное решение не хуже
     оптимального на каждом шаге
  2. → В конце жадное не хуже оптимального

МЕТОД 3: Структурная индукция
  1. База: для маленьких n жадное = оптимальное
  2. Переход: жадный выбор сохраняет свойство
  3. → Жадное решение оптимально

Пример (Activity Selection):
  Утверждение: Выбор активности с ранним концом оптимален
  Доказательство: Чем раньше освобождаемся,
    тем больше времени для других активностей
  → Заменив любой выбор на более ранний,
    не ухудшим решение
""")

# ============================================================
# 9. КОГДА GREEDY НЕ РАБОТАЕТ
# ============================================================

print("\n\n9. КОГДА ЖАДНЫЙ ПОДХОД НЕ РАБОТАЕТ")
print("-" * 60)

print("""
❌ 0/1 KNAPSACK (целочисленный рюкзак)
   Нельзя брать части → жадный не работает
   Решение: Динамическое программирование

❌ COIN CHANGE (для неканонических систем)
   Например: [1, 3, 4] для amount=6
   Жадный: [4, 1, 1] = 3 монеты
   Оптимум: [3, 3] = 2 монеты
   Решение: Динамическое программирование

❌ LONGEST PATH (максимальный путь)
   Жадный выбор может отрезать оптимальный путь
   Решение: Полный перебор или DP

❌ LONGEST COMMON SUBSEQUENCE
   Нет жадного критерия
   Решение: Динамическое программирование

ПРАВИЛО: Если сомневаетесь - попробуйте найти контрпример!
""")

# Демонстрация: 0/1 Knapsack
print("\nПример: 0/1 Knapsack (НЕ работает жадный):")
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50

print(f"Предметы: {items}")
print(f"Вместимость: {capacity}")

print("\nЖадный подход (value/weight):")
print("  Берём (10, 60): 6₽/кг")
print("  Берём (20, 100): 5₽/кг")
print("  Не влезает (30, 120)")
print("  Итого: 160₽")

print("\nОптимум:")
print("  Берём (20, 100) + (30, 120) = 220₽")
print("  ✗ Жадный дал НЕОПТИМАЛЬНЫЙ ответ!")

# ============================================================
# 10. ЗАДАЧИ ДЛЯ ПРАКТИКИ
# ============================================================

print("\n\n10. ЗАДАЧИ ДЛЯ ПРАКТИКИ")
print("-" * 60)

print("""
ЛЕГКИЕ:
  1. LeetCode #455 - Assign Cookies
  2. LeetCode #860 - Lemonade Change
  3. LeetCode #1221 - Split Balanced Strings

СРЕДНИЕ:
  4. LeetCode #55 - Jump Game
  5. LeetCode #45 - Jump Game II
  6. LeetCode #134 - Gas Station
  7. LeetCode #435 - Non-overlapping Intervals
  8. LeetCode #452 - Minimum Arrows to Burst Balloons

СЛОЖНЫЕ:
  9. LeetCode #135 - Candy
  10. LeetCode #621 - Task Scheduler
  11. LeetCode #765 - Couples Holding Hands

CODEFORCES:
  - Задачи с тегом "greedy"
  - Сложность 900-1200 для начала
""")

print("\n" + "=" * 60)
print("ИТОГИ")
print("=" * 60)

print("""
✅ Жадный алгоритм: локально оптимальный выбор → глобальный оптимум

✅ Классические жадные задачи:
   • Activity Selection - сортировка по концу
   • Fractional Knapsack - сортировка по value/weight
   • Huffman Coding - приоритетная очередь

✅ Когда работает:
   • Можно доказать корректность
   • Задача имеет свойство жадного выбора

❌ Когда НЕ работает:
   • 0/1 Knapsack (нужен DP)
   • Неканонические системы монет (нужен DP)
   • LCS, Edit Distance (нужен DP)

💡 Совет: Если жадный кажется очевидным - проверьте контрпример!
   Если контрпример есть → нужен DP

🔍 Как проверить: попробуйте найти случай, где жадный не работает
""")

print("=" * 60)
