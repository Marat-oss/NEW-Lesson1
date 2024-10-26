my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
a = my_list[i]
while a > -1:
    print(a)
    i = i + 1
    if (i < len(my_list)):
        a = my_list[i]
    else:
        break
