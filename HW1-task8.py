__author__ = 'dashik'
a = int(input('Ведите длину отрезка '))
b = int(input('Ведите длину отрезка '))
c = int(input('Ведите длину отрезка '))
if a + b <= c or a + c <= b or c + b <= a:
    print('Треугольник не может быть построен')
else:
    if a == b and b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or c == a:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')