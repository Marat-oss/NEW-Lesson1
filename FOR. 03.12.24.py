# 1:  Найти произведение всех целых  чисел от 1 до 10.
# Решение с помощью  цикла for.
# n = 0
# for i in range(1, 11):
#     for j in range(1, 11):
#         n = j * i
#         print(n)


# 2: Найти сумму  чисел от 10 до 50, кратных 3.
# Решение с помощью  цикла for.
# n = 0
# for i in range(10, 51):
#     if i % 3 == 0:
#         n += i
# print(n)

# 3: Дано два числа: a и b, a<b. Напечатать в столбик и строчку все числа от a до b
# включительно, а также квадраты этих чисел.
# a = int(input("Введите первое число: "))
# b = int(input("Введите число, больше первого: "))
# n = 0
# s = 0
# for j in range(a, b + 1):
#     n = j ** 2
#     print(n)
# for i in range(a, b + 1):
#     s = i
#     print(s, end="")

# 4: Дано два целых числа: a1 и a2. Если a1<a2, то напечатайте числа от a1 до a2
# в порядке возрастания. В противном случае, напечатайте числа от a1 до a2 в порядке убывания.
# a1 = int(input("Введите число: "))
# a2 = int(input("Введите число: "))
# for i in range(a1, a2 + 1):
#     if a1 < a2:
#         print(i)
# else:
#     for i in range(a1, a2 - 1, -1):
#         print(i)

# 5: Дано число k. Вычислите сумму квадратов нечетных чисел от 1 до k.
# k = int(input("Введите число: "))
# n = 0
# s = 0
# for i in range(1, k + 1):
#     if i % 2 != 0:
#         n = i ** 2
#         s = n + 1
#         print(s)

# 6: Дано число n. Мы вводим это число, а затем ровно n натуральных чисел.
# Посчитать, сколько среди этих чисел кратных трем.
# n = int(input("Введите число: "))
# k = 0
# i = 0
# s = []
# j = 0
# while i <= n - 1:
#         i+= 1
#         k = int(input("Введите число: "))
#         if k % 3 == 0:
#             s.append(k)
# for j in range(len(s)):
#     j += 1
# print(j)


