# Решения задач - Этап 1

Здесь собраны детальные решения ключевых задач с объяснениями.

---

## Задача 1: Way Too Long Words
**Платформа:** [Codeforces 71A](https://codeforces.com/problemset/problem/71/A)
**Сложность:** 800

### Условие
Слова длиннее 10 символов сокращать до формата: первая буква + количество средних букв + последняя буква.

### Формат ввода
```
3
word
localization
internationalization
```

### Формат вывода
```
word
l10n
i18n
```

### Решение
```python
def solve():
    word = input().strip()

    if len(word) <= 10:
        print(word)
    else:
        # Первая + кол-во средних + последняя
        shortened = word[0] + str(len(word) - 2) + word[-1]
        print(shortened)

# Несколько тестов
t = int(input())
for _ in range(t):
    solve()
```

### Объяснение
1. Читаем количество тестов
2. Для каждого слова:
   - Если длина ≤ 10 — выводим как есть
   - Иначе: первый символ + (длина - 2) + последний символ
3. `word[0]` — первый символ, `word[-1]` — последний

**Сложность:** O(1) для каждого слова

---

## Задача 2: Two Sum
**Платформа:** [LeetCode #1](https://leetcode.com/problems/two-sum/)
**Сложность:** Easy

### Условие
Дан массив целых чисел `nums` и число `target`. Найти индексы двух чисел, сумма которых равна `target`.

### Пример
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

### Решение 1: Наивное (O(n²))
```python
def two_sum_naive(nums, target):
    """Проверяем все пары"""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

**Проблема:** Для каждого элемента проверяем все остальные — медленно!

### Решение 2: С использованием словаря (O(n))
```python
def two_sum(nums, target):
    """Оптимальное решение"""
    seen = {}  # число -> его индекс

    for i, num in enumerate(nums):
        complement = target - num

        # Проверяем, видели ли complement раньше
        if complement in seen:
            return [seen[complement], i]

        # Запоминаем текущее число
        seen[num] = i

    return []
```

### Объяснение
1. Для каждого числа `num` ищем `complement = target - num`
2. Если `complement` уже в словаре — нашли пару!
3. Иначе запоминаем текущее число

**Почему быстрее?**
- Словарь: поиск за O(1)
- Проходим массив один раз: O(n)
- Итого: O(n) вместо O(n²)

---

## Задача 3: Valid Anagram
**Платформа:** [LeetCode #242](https://leetcode.com/problems/valid-anagram/)
**Сложность:** Easy

### Условие
Проверить, являются ли две строки анаграммами (содержат одинаковые буквы).

### Пример
```
Input: s = "anagram", t = "nagaram"
Output: true
```

### Решение 1: Сортировка
```python
def is_anagram_sort(s, t):
    return sorted(s) == sorted(t)
```

**Сложность:** O(n log n) из-за сортировки

### Решение 2: Counter
```python
from collections import Counter

def is_anagram_counter(s, t):
    return Counter(s) == Counter(t)
```

**Сложность:** O(n)

### Решение 3: Словарь вручную
```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    # Считаем буквы в s
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Вычитаем буквы из t
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True
```

### Объяснение
- Counter автоматически подсчитывает частоты
- Сравнение Counter'ов проверяет равенство частот
- Решение 3 делает то же самое вручную

---

## Задача 4: Maximum Subarray (Kadane's Algorithm)
**Платформа:** [LeetCode #53](https://leetcode.com/problems/maximum-subarray/)
**Сложность:** Medium

### Условие
Найти подмассив с максимальной суммой.

### Пример
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
```

### Решение: Алгоритм Кадане
```python
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        # Продолжить или начать заново?
        current_sum = max(nums[i], current_sum + nums[i])

        # Обновить максимум
        max_sum = max(max_sum, current_sum)

    return max_sum
```

### Объяснение
**Идея:** На каждой позиции выбираем:
1. Начать новый подмассив с текущего элемента
2. Продолжить предыдущий подмассив

**Пример пошагово:**
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i=0: current=-2, max=-2
i=1: current=max(1, -2+1)=1, max=1
i=2: current=max(-3, 1-3)=-2, max=1
i=3: current=max(4, -2+4)=4, max=4
i=4: current=max(-1, 4-1)=3, max=4
i=5: current=max(2, 3+2)=5, max=5
i=6: current=max(1, 5+1)=6, max=6
i=7: current=max(-5, 6-5)=1, max=6
i=8: current=max(4, 1+4)=5, max=6
```

**Ответ:** 6

---

## Задача 5: Valid Palindrome
**Платформа:** [LeetCode #125](https://leetcode.com/problems/valid-palindrome/)
**Сложность:** Easy

### Условие
Проверить, является ли строка палиндромом (учитывать только буквы и цифры, игнорировать регистр).

### Пример
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

### Решение 1: Два указателя
```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # Пропускаем не-буквы/цифры
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Сравниваем
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### Решение 2: Простое (но медленнее)
```python
def is_palindrome_simple(s):
    # Оставляем только буквы/цифры в нижнем регистре
    clean = ''.join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]
```

### Объяснение
- **Решение 1:** Два указателя с концов, O(n) времени, O(1) памяти
- **Решение 2:** Создаем новую строку, O(n) времени и памяти

---

## Задача 6: Container With Most Water
**Платформа:** [LeetCode #11](https://leetcode.com/problems/container-with-most-water/)
**Сложность:** Medium

### Условие
Дан массив высот. Найти две линии, образующие контейнер с максимальной площадью.

### Пример
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

### Решение: Два указателя
```python
def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Вычисляем площадь
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        max_water = max(max_water, area)

        # Двигаем меньший указатель
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

### Объяснение
**Почему двигаем меньший указатель?**

Площадь = ширина × min(высоты)

При движении:
- Ширина всегда уменьшается
- Чтобы увеличить площадь, нужно увеличить высоту
- Двигая **больший** указатель, высота может только уменьшиться!
- Двигая **меньший**, есть шанс найти бóльшую высоту

**Пример:**
```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
          L                       R

Площадь = 8 × min(1,7) = 8 × 1 = 8
Двигаем L (меньший)

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
             L                    R

Площадь = 7 × min(8,7) = 7 × 7 = 49 ✓
```

---

## Задача 7: Longest Substring Without Repeating Characters
**Платформа:** [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
**Сложность:** Medium

### Условие
Найти длину самой длинной подстроки без повторяющихся символов.

### Пример
```
Input: s = "abcabcbb"
Output: 3
Explanation: "abc"
```

### Решение: Скользящее окно
```python
def longest_substring_no_repeats(s):
    char_index = {}  # символ -> последний индекс
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        # Если символ в текущем окне
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Объяснение пошагово

```
s = "abcabcbb"

right=0, char='a': окно="a", left=0, len=1
right=1, char='b': окно="ab", left=0, len=2
right=2, char='c': окно="abc", left=0, len=3
right=3, char='a': дубликат! left=1, окно="bca", len=3
right=4, char='b': дубликат! left=2, окно="cab", len=3
right=5, char='c': дубликат! left=3, окно="abc", len=3
right=6, char='b': дубликат! left=5, окно="cb", len=2
right=7, char='b': дубликат! left=7, окно="b", len=1

Максимум: 3
```

**Ключевая идея:** При повторе символа сдвигаем левую границу за предыдущее вхождение.

---

## Задача 8: Find First and Last Position
**Платформа:** [LeetCode #34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
**Сложность:** Medium

### Условие
Найти первое и последнее вхождение элемента в отсортированном массиве.

### Пример
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Решение: bisect
```python
import bisect

def find_first_last(nums, target):
    left = bisect.bisect_left(nums, target)

    # Проверяем наличие
    if left == len(nums) or nums[left] != target:
        return [-1, -1]

    right = bisect.bisect_right(nums, target) - 1
    return [left, right]
```

### Решение без bisect
```python
def find_first_last_manual(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid
                right = mid - 1  # ищем левее
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
                result = mid
                left = mid + 1  # ищем правее
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

### Объяснение
**bisect_left:** Находит первую позицию, где можно вставить элемент
**bisect_right:** Находит позицию после последнего вхождения

Пример:
```
nums = [5, 7, 7, 8, 8, 10], target = 8

bisect_left(nums, 8) = 3   (первое вхождение)
bisect_right(nums, 8) = 5  (после последнего)
Последнее = 5 - 1 = 4
```

---

## Полезные ссылки

### Практика по темам
- [LeetCode - Two Pointers](https://leetcode.com/tag/two-pointers/)
- [LeetCode - Sliding Window](https://leetcode.com/tag/sliding-window/)
- [LeetCode - Hash Table](https://leetcode.com/tag/hash-table/)
- [Codeforces - Rating 800-1000](https://codeforces.com/problemset?tags=800-1000)

### Разбор задач
- [NeetCode - LeetCode Solutions](https://neetcode.io/)
- [Codeforces - Editorials](https://codeforces.com/blog/entry/92977)

Удачи в решении задач! 🚀
