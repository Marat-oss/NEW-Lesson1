def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range (m):
                matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input("Введите количество строк в матрице: "))
m = int(input("Введите количество столбцов в матрице: "))
value = input(f'Введите значения матрицы: ')
print('-----' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
        print("Неверное значение количнства строк")
elif m <= 0:
        print("Неверное значение количества столбцов")
else:
    print("Матрица воплоти")
    for i in matrix:
            print(*i)
