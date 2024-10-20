immutable_var = (2, 'Banana', 3 , 1.5)
print(type(immutable_var))
print(immutable_var)
#immutable_var[1]='Peach' # Элементы в кортеже не изменяемы
mutable_list=["Lion", "dog", "1.5", "1"]
print(type(mutable_list))
print(mutable_list)
mutable_list[2]='3.5'
mutable_list[1]='cool python'
print(mutable_list)

