# 1.	Подсчет символов в строке
# Напишите программу, которая запрашивает строку у пользователя и с
# помощью цикла while считает количество символов в строке, используя len.


#text = input("Введите текст: ")
# a = 0
# while a < len(text):
#         a += 1
# print(a)

#2.	Обход списка с выводом элементов
#Дано: список чисел. Используя цикл while и len, выведите
# по одному каждый элемент списка.

# number_list = [1, 2, 3, 4, 5, 6, 7]
# a = 0
# while a < len(number_list):
#         a += 1
#         print(a)

#3.	Реверс строки
# Запросите строку у пользователя. Используя цикл while и len,
# выведите строку в обратном порядке.

# text_str = input("Введите текст: ")
#                                   # a = text_str[::-1]
#                                   # print(a)
# i = 0
# j = 0
# b = ""
# while j < len(text_str):
#     if text_str[i] != 0:
#         j += 1
#         i -= 1
#         b += text_str[i]
# print(b)





# 4. Сумма элементов списка

# number_list = [1, 2, 3, 4, 5]
# a = 0
# b = 0
# while a < len(number_list):
#     b = b + number_list[a]
#     a += 1
# print(b)

# 5. Поиск символа в строке.
# Напишите программу, которая проверяет, есть ли заданный символ в строке.
# Используйте while для перебора строки и сравнения символов.

# el_str = input("Введите данные текста: ")
# element = 'a'
# i = 0
# b = 0
# while i < len(el_str):
#     if el_str[i] == element:
#         print("Есть элемент")
#         b = b + 1
#     i += 1
# if b == 0:
#     print("Элемент не найден.")



# 6.	Удаление элементов из списка
# Дано: список строк. Используя цикл while и len, удалите элементы из
# списка один за другим, пока он не станет пустым.

# element_list = ['Sasha', 'Pavel', 'Magaazin', 'cww']
# i = 0
# while i < len(element_list):
#     if element_list[i] != 0:
#         del element_list[i]
#     print(element_list)
# i += 1


#7	Подсчет слов в строке. Запросите строку у пользователя.
# Считайте количество слов в строке (слова разделены пробелами)
# с использованием len и цикла while.

# el_str = input("Введите предложение: ")
# words = el_str.split()
# print(words)
# i = 0
# while i < len(words):
#     i += 1
# print(i)

# 8.	Минимальный элемент в списке
# Дано: список чисел. Найдите минимальный элемент в списке, используя цикл while и len.

# number_list = [101, 123, 233, 42, 6453, 322, 31]
# # number_list.sort()
# # print(number_list[0])
# min = number_list[0]
# i = 0
# min_num = []
# while i < len(number_list):
#     if number_list[i] < min:
#         min = number_list[i]
#     i += 1
# print("Наименьшее число в списке: " , min)


# 9.	Удаление всех пробелов в строке
# Запросите строку у пользователя. Используя while и len,
# удалите из строки все пробелы и выведите результат.
# Сложные задачи

# text = input("Введите текст: ")
# symbols = list(text)
# # print(symbols)
# i = 0
# a = ' '
# while i < len(symbols):
#     if symbols[i] != a:
#         i += 1
#     elif symbols[i] == a:
#         del symbols[i]
# b = ''.join(symbols)
# print(b)

# 10.	Объединение двух списков
# Дано: два списка одинаковой длины. С помощью while и len создайте третий список,
# где элементы из первого и второго списков чередуются.
#
# Пример:
# Вход: [1, 2, 3], ['a', 'b', 'c']
# Выход: [1, 'a', 2, 'b', 3, 'c']

# numbers = [1, 2, 3]
# elements = ['a', 'b', 'c']
# num_el = []
# #print(elements)
# i = 0
# j = 0
# while i < len(numbers) and j < len(elements):
#     num_el.append(numbers[i])
#     num_el.append(elements[j])
#     i += 1
#     j += 1
# print(num_el)





