first=int(input('Введите первое число: '))
second=int(input('Ввудите второе число: '))
third=int(input('Введите третье число: '))
if first==second and second==third and third==first:
    print(3)
elif first==second or first==third or third==second:
    print(2)
elif first!=second and second!=third and third!=first:
    print(0)
else:print('Число не подходит') #Это же можно наверное вообще не прописывать, в условиях данной задачи?
