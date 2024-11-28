 1. Дан список с числами:
Найдите сумму элементов этого списка.


 numbers = [1, 2, 3, 4, 5]
 print(sum(numbers))

 2. Дан список с числами:
 Найдите сумму квадратов элементов этого списка.

 numbers = [1, 2, 3, 4, 5]
 i = 0
 a = []
 b = 0
 while i < len(numbers):
     b = numbers[i] ** 2
     i += 1
     a.append(b)
 print(sum(a))

 3.Дан список с числами:
 Найдите сумму квадратных корней элементов этого списка.

 numbers = [1, 2, 3, 4, 5]
 i = 0
 a = []
 b = 0
 while i < len(numbers):
     b = numbers[i] ** 0.5
     i += 1
     a.append(b)
 print(sum(a))


 4.Дан список с числами:
 Найдите сумму положительных элементов этого списка.

 numbers = [1, 2, -3, 4, -5]
 i = 0
 b = []
 c = []
 while i < len(numbers):
     if numbers[i] < 1:
         c.append(numbers[i])
         i += 1
     elif numbers[i] >= 1:
         b.append(numbers[i])
         i += 1
 print(sum(b))

 5. Дан список с числами:
 Найдите сумму тех элементов этого списка, которые больше нуля и меньше десяти.

 numbers = [-1, 2, -3, 4, 5, 11]
 i = 0
 a = []
 b = []
 while i < len(numbers):
    if numbers[i] >= 1:
         a.append(numbers[i])
         i += 1
     elif numbers[i] < 1:
         b.append(numbers[i])
         i += 1
 print(sum(a))

 6. Дана некоторая строка:
 Переберите и выведите в консоль по очереди все символы с конца строки.

 elements = 'abcde'
 el_list = list(elements)
 print(el_list)
 i = -1
 a = []
 while i < len(el_list):
     if i > -6:
         a.append(el_list[i])
         i -= 1
         continue
     break
 print(a)
 s = "".join(a)
 print(s)

 ДЗ
 Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
 Нужно выписывать из этого списка только положительные числа до тех пор,
 пока не встретите отрицательное или не закончится список (выход за границу).
 Пункты задачи:
1. Запишите исходный список в переменную my_list.
2. Напишите цикл while с соответствующими задаче условиями.
3. Используйте операторы прерывания/продолжения
 цикла в соответствии с условиями задачи.

 my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
 i = 0
 a = []
 while i < len(my_list):
     a.append(my_list[i])
     i += 1
     if my_list[i] < 0:
         break
 print(a)



