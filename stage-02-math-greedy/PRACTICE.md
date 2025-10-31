# Практические задачи - Этап 2: Математика и жадные алгоритмы

## Как использовать этот файл

1. Решайте задачи по порядку (от легких к сложным)
2. Сначала попробуйте решить сами (15-30 минут)
3. Если не получается - посмотрите подсказку
4. Если все равно сложно - посмотрите решение в SOLUTIONS.md
5. После решения попробуйте оптимизировать код

---

## Уровень 1: Основы математики и простой greedy (Легкие)

### Задача 1.1: НОД двух чисел
**Платформа:** [LeetCode #1979 - Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | **Сложность:** Easy

**Условие:** Найти НОД наименьшего и наибольшего элемента массива.

**Пример:**
```
Вход: nums = [2,5,6,9,10]
Выход: 2
Объяснение: min = 2, max = 10, НОД(2,10) = 2
```

**Подсказка:** Используйте алгоритм Евклида или `math.gcd()`

---

### Задача 1.2: Степень числа 2
**Платформа:** [LeetCode #231 - Power of Two](https://leetcode.com/problems/power-of-two/) | **Сложность:** Easy

**Условие:** Определить, является ли число степенью двойки.

**Пример:**
```
Вход: n = 16
Выход: True (2^4 = 16)

Вход: n = 3
Выход: False
```

**Подсказка:** Можно использовать битовые операции: степень двойки имеет только один бит равный 1

---

### Задача 1.3: FizzBuzz (делимость)
**Платформа:** [LeetCode #412 - Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | **Сложность:** Easy

**Условие:** Для чисел от 1 до n:
- Если делится на 3: выведите "Fizz"
- Если делится на 5: выведите "Buzz"
- Если делится на оба: выведите "FizzBuzz"
- Иначе: выведите само число

**Пример:**
```
Вход: n = 5
Выход: ["1","2","Fizz","4","Buzz"]
```

**Подсказка:** Проверяйте делимость с помощью оператора %

---

### Задача 1.4: Счастливое число
**Платформа:** [LeetCode #202 - Happy Number](https://leetcode.com/problems/happy-number/) | **Сложность:** Easy

**Условие:** Число называется счастливым, если повторяя процесс замены числа на сумму квадратов его цифр, в итоге получаем 1.

**Пример:**
```
Вход: n = 19
Выход: True
Объяснение:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
```

**Подсказка:** Используйте set для отслеживания уже виденных чисел (цикл = не счастливое)

---

### Задача 1.5: Монеты для сдачи (жадный)
**Платформа:** [LeetCode #860 - Lemonade Change](https://leetcode.com/problems/lemonade-change/) | **Сложность:** Easy

**Условие:** Продаёте лимонад за $5. Покупатели платят купюрами $5, $10, $20. Можете ли вы дать сдачу всем? Изначально сдачи нет.

**Пример:**
```
Вход: bills = [5,5,5,10,20]
Выход: True

Вход: bills = [5,5,10,10,20]
Выход: False
```

**Подсказка:** Жадно используйте крупные купюры для сдачи

---

## Уровень 2: Средняя сложность (Medium)

### Задача 2.1: Числа Фибоначчи
**Платформа:** [LeetCode #509 - Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | **Сложность:** Easy

**Условие:** Вычислить n-е число Фибоначчи.

**Пример:**
```
Вход: n = 4
Выход: 3
Объяснение: F(4) = F(3) + F(2) = 2 + 1 = 3
```

**Подсказка:** Не используйте рекурсию - O(n) с двумя переменными

---

### Задача 2.2: Биномиальные коэффициенты
**Платформа:** [LeetCode #118 - Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | **Сложность:** Easy

**Условие:** Построить первые n строк треугольника Паскаля.

**Пример:**
```
Вход: numRows = 5
Выход:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

**Подсказка:** C(n, k) = C(n-1, k-1) + C(n-1, k)

---

### Задача 2.3: Множители простых чисел
**Платформа:** [LeetCode #762 - Prime Number of Set Bits](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) | **Сложность:** Easy

**Условие:** Подсчитать числа в диапазоне [left, right], у которых количество единичных битов - простое число.

**Пример:**
```
Вход: left = 6, right = 10
Выход: 4
Объяснение:
6 -> 110 (2 единицы, 2 - простое) ✓
7 -> 111 (3 единицы, 3 - простое) ✓
9 -> 1001 (2 единицы, 2 - простое) ✓
10 -> 1010 (2 единицы, 2 - простое) ✓
```

**Подсказка:** bin(n).count('1') для подсчета битов

---

### Задача 2.4: Перестановка монет
**Платформа:** [LeetCode #322 - Coin Change](https://leetcode.com/problems/coin-change/) | **Сложность:** Medium

**Условие:** Дан массив номиналов монет и сумма. Найти минимальное количество монет для получения суммы.

**Пример:**
```
Вход: coins = [1,2,5], amount = 11
Выход: 3
Объяснение: 11 = 5 + 5 + 1
```

**Подсказка:** Жадный подход НЕ работает для произвольных монет! Используйте динамическое программирование.

---

### Задача 2.5: Минимум интервалов для покрытия
**Платформа:** [LeetCode #452 - Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | **Сложность:** Medium

**Условие:** Есть шарики на числовой оси, каждый покрывает диапазон [start, end]. Найти минимальное количество стрел, чтобы лопнуть все шарики. Стрела в точке x лопает все шарики, содержащие x.

**Пример:**
```
Вход: points = [[10,16],[2,8],[1,6],[7,12]]
Выход: 2
Объяснение: Стрелы в x=6 и x=11
```

**Подсказка:** Сортировка по концу интервала + жадный выбор

---

### Задача 2.6: Раздача печенек
**Платформа:** [LeetCode #455 - Assign Cookies](https://leetcode.com/problems/assign-cookies/) | **Сложность:** Easy

**Условие:** Дети с жадностью g[i] и печеньки с размером s[j]. Ребёнок доволен, если s[j] >= g[i]. Максимизировать количество довольных детей.

**Пример:**
```
Вход: g = [1,2,3], s = [1,1]
Выход: 1
Объяснение: Даём печеньку размера 1 ребёнку с жадностью 1
```

**Подсказка:** Отсортируйте оба массива, жадно назначайте печеньки

---

### Задача 2.7: Максимум единиц в грузовике
**Платформа:** [LeetCode #1710 - Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) | **Сложность:** Easy

**Условие:** Грузовик вмещает truckSize коробок. Дан массив boxTypes[i] = [numberOfBoxes, unitsPerBox]. Максимизировать количество единиц товара в грузовике.

**Пример:**
```
Вход: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Выход: 8
Объяснение: Берём 1 коробку (3 единицы) + 2 коробки (2*2=4 единицы) + 1 коробку (1 единица) = 8
```

**Подсказка:** Жадно берите коробки с максимальным unitsPerBox

---

## Уровень 3: Продвинутые (Сложные)

### Задача 3.1: Разбиение на k равных подмножеств
**Платформа:** [LeetCode #698 - Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | **Сложность:** Medium

**Условие:** Можно ли разбить массив на k подмножеств с равными суммами?

**Пример:**
```
Вход: nums = [4,3,2,3,5,2,1], k = 4
Выход: True
Объяснение: [5], [1,4], [2,3], [2,3]
```

**Подсказка:** Сумма всех элементов должна делиться на k. Используйте backtracking.

---

### Задача 3.2: Купить и продать акции с ограничением
**Платформа:** [LeetCode #714 - Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | **Сложность:** Medium

**Условие:** Как в задаче Stock II, но каждая сделка стоит fee.

**Пример:**
```
Вход: prices = [1,3,2,8,4,9], fee = 2
Выход: 8
Объяснение: Купить день 1 (цена 1), продать день 4 (цена 8), прибыль = 8-1-2 = 5
            Купить день 5 (цена 4), продать день 6 (цена 9), прибыль = 9-4-2 = 3
            Итого: 5 + 3 = 8
```

**Подсказка:** Динамическое программирование или жадный с отслеживанием состояний

---

### Задача 3.3: Расстановка стульев
**Платформа:** [LeetCode #849 - Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/) | **Сложность:** Medium

**Условие:** Ряд стульев, 1 = занят, 0 = свободен. Найти место, максимизирующее расстояние до ближайшего человека.

**Пример:**
```
Вход: seats = [1,0,0,0,1,0,1]
Выход: 2
Объяснение: Сесть на индекс 2, расстояние min(2, 2) = 2
```

**Подсказка:** Найдите максимальный промежуток между единицами, учтите края

---

### Задача 3.4: Планировщик задач
**Платформа:** [LeetCode #621 - Task Scheduler](https://leetcode.com/problems/task-scheduler/) | **Сложность:** Medium

**Условие:** Даны задачи с типами A-Z. Между одинаковыми задачами нужен интервал n. Найти минимальное время выполнения всех задач.

**Пример:**
```
Вход: tasks = ["A","A","A","B","B","B"], n = 2
Выход: 8
Объяснение: A -> B -> idle -> A -> B -> idle -> A -> B
```

**Подсказка:** Жадно планируйте самые частые задачи

---

## Задачи с Codeforces

### CF 2.1: Sum of Round Numbers
**Сложность:** 800
**Условие:** Представить число как сумму "круглых" чисел (10, 20, 300, 5000, ...).

**Пример:**
```
Вход: 5009
Выход: 2
5000 9
```

**Ссылка:** [Codeforces 1352A](https://codeforces.com/problemset/problem/1352/A)

---

### CF 2.2: Anton and Danik
**Сложность:** 800
**Условие:** Строка из 'A' и 'D'. Кого больше?

**Ссылка:** [Codeforces 734A](https://codeforces.com/problemset/problem/734/A)

---

### CF 2.3: Bear and Big Brother
**Сложность:** 800
**Условие:** Лимак весит a, брат весит b. Лимак утраивается каждый год, брат удваивается. Через сколько лет Лимак станет строго тяжелее?

**Ссылка:** [Codeforces 791A](https://codeforces.com/problemset/problem/791/A)

---

### CF 2.4: Helpful Maths
**Сложность:** 800
**Условие:** Дана строка с суммой чисел (например "3+2+1"). Отсортировать числа в порядке возрастания.

**Пример:**
```
Вход: "3+2+1"
Выход: "1+2+3"
```

**Ссылка:** [Codeforces 339A](https://codeforces.com/problemset/problem/339/A)

---

### CF 2.5: Word Capitalization
**Сложность:** 800
**Условие:** Сделать первую букву заглавной.

**Ссылка:** [Codeforces 281A](https://codeforces.com/problemset/problem/281/A)

---

### CF 2.6: Soldier and Bananas
**Сложность:** 800
**Условие:** Первый банан стоит k, второй 2k, третий 3k, ... Сколько нужно занять, если есть n долларов и нужно купить w бананов?

**Ссылка:** [Codeforces 546A](https://codeforces.com/problemset/problem/546/A)

---

### CF 2.7: Boy or Girl
**Сложность:** 800
**Условие:** Подсчитать количество уникальных символов. Если чётное - "CHAT WITH HER!", иначе - "IGNORE HIM!".

**Ссылка:** [Codeforces 236A](https://codeforces.com/problemset/problem/236/A)

---

### CF 2.8: Stones on the Table
**Сложность:** 800
**Условие:** Камни стоят в ряд (R, G, B). Минимум камней для удаления, чтобы соседние были разных цветов.

**Ссылка:** [Codeforces 266A](https://codeforces.com/problemset/problem/266/A)

---

### CF 2.9: Presents
**Сложность:** 800
**Условие:** Дан массив p, где p[i] - кому i-й друг подарил подарок. Вывести обратный массив: кто подарил каждому.

**Ссылка:** [Codeforces 136A](https://codeforces.com/problemset/problem/136/A)

---

### CF 2.10: Tram
**Сложность:** 800
**Условие:** На каждой остановке exit[i] выходят, enter[i] входят. Найти минимальную вместимость трамвая.

**Ссылка:** [Codeforces 116A](https://codeforces.com/problemset/problem/116/A)

---

## Дополнительные задачи по темам

### Математика - Простые числа
1. [LeetCode #204 - Count Primes](https://leetcode.com/problems/count-primes/) - Easy
2. [LeetCode #263 - Ugly Number](https://leetcode.com/problems/ugly-number/) - Easy
3. [LeetCode #264 - Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) - Medium

### Математика - Степени
1. [LeetCode #50 - Pow(x, n)](https://leetcode.com/problems/powx-n/) - Medium
2. [LeetCode #372 - Super Pow](https://leetcode.com/problems/super-pow/) - Medium

### Математика - Комбинаторика
1. [LeetCode #62 - Unique Paths](https://leetcode.com/problems/unique-paths/) - Medium
2. [LeetCode #119 - Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) - Easy

### Жадные - Интервалы
1. [LeetCode #56 - Merge Intervals](https://leetcode.com/problems/merge-intervals/) - Medium
2. [LeetCode #57 - Insert Interval](https://leetcode.com/problems/insert-interval/) - Medium
3. [LeetCode #253 - Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) - Medium (Premium)

### Жадные - Оптимизация
1. [LeetCode #1005 - Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) - Easy
2. [LeetCode #1221 - Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) - Easy

---

## План на неделю

### Неделя 1: Математика (НОД, простые числа)

**День 1-2:**
- Решите задачи 1.1 - 1.4 (основы математики)
- Запустите примеры из `examples/01_gcd_lcm.py`
- Изучите алгоритм Евклида

**День 3-4:**
- Решите задачу 2.1 (Фибоначчи)
- Решите задачу 2.2 (Треугольник Паскаля)
- Попробуйте задачи CF 2.1 - 2.3

**День 5-6:**
- Решите задачу 2.3 (простые числа)
- Запустите примеры из `examples/02_prime_numbers.py`
- Попробуйте дополнительные задачи на простые числа

**День 7:**
- Решите задачи CF 2.4 - 2.6
- Повторите материал

### Неделя 2: Жадные алгоритмы

**День 1-2:**
- Изучите теорию жадных алгоритмов в README.md
- Решите задачу 1.5 (Lemonade Change)
- Решите задачу 2.6 (Assign Cookies)
- Решите задачу 2.7 (Maximum Units on Truck)

**День 3-4:**
- Решите задачу 2.5 (Arrows to Burst Balloons)
- Изучите Jump Game из README
- Попробуйте решить Jump Game самостоятельно

**День 5-6:**
- Попробуйте задачу 3.4 (Task Scheduler)
- Решите задачи CF 2.7 - 2.10
- Дополнительно: задачи на интервалы

**День 7:**
- Виртуальный контест на Codeforces (Div 3 или Div 4)
- Разберите решения

### Неделя 3: Продвинутые задачи

**День 1-3:**
- Решите задачу 3.1 (Partition to K Subsets)
- Решите задачу 3.2 (Stock with Fee)
- Изучите решения из SOLUTIONS.md

**День 4-7:**
- Решите дополнительные задачи по темам
- Участвуйте в реальном контесте на Codeforces
- Решайте задачи сложности 900-1100

---

## Критерии готовности к следующему этапу

Вы готовы к Этапу 3 (Рекурсия и перебор), если:

- ✅ Решили минимум 12 задач уровня 1
- ✅ Решили минимум 10 задач уровня 2
- ✅ Понимаете алгоритм Евклида для НОД
- ✅ Знаете решето Эратосфена
- ✅ Понимаете быстрое возведение в степень
- ✅ Знакомы с базовой комбинаторикой
- ✅ Понимаете, когда жадный подход работает
- ✅ Решаете задачи Codeforces 800-900 за 10-15 минут
- ✅ Можете доказать корректность простого жадного алгоритма

---

## Полезные ресурсы

### Математика
- [CP-Algorithms: GCD](https://cp-algorithms.com/algebra/euclid-algorithm.html)
- [CP-Algorithms: Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)
- [CP-Algorithms: Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html)

### Жадные алгоритмы
- [USACO Guide: Greedy Algorithms](https://usaco.guide/bronze/greedy-sorting)
- [CP-Algorithms: Activity Selection](https://cp-algorithms.com/schedules/schedule_one_machine.html)

### Платформы
- [Codeforces: Math Problems](https://codeforces.com/problemset?tags=math)
- [Codeforces: Greedy Problems](https://codeforces.com/problemset?tags=greedy)
- [LeetCode: Math Tag](https://leetcode.com/tag/math/)
- [LeetCode: Greedy Tag](https://leetcode.com/tag/greedy/)

---

Удачи в решении задач! Помните: математика и жадные алгоритмы - основа для более сложных тем.
