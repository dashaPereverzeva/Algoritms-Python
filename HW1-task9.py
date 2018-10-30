__author__ = 'dashik'

a = int(input('Введите число '))
b = int(input('Введите еще одно число '))
c = int(input('Введите еще одно число '))
if (a > b and b > c) or (c > b and b > a):
    print('среднее', b)
elif (a > c and c > b) or (b>c and c>a):
    print('среднее', c)
elif (c > a and a > b) or (b>a and a>c):
    print(a)
else:
    print('Решения нет')

