__author__ = 'dashik'
El1 = input('Введите букву латинского алфавита ')
El2 = input('Введите еще одну букву латинского алфавита ')
Alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
       'x', 'y', 'z']
print(Alf.index(El1))
print(Alf.index(El2))
Def = abs(Alf.index(El1) - Alf.index(El2)) - 1
print(Def)