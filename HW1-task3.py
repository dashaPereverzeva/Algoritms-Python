__author__ = 'dashik'

X1 = int(input("Введите значение x точки 1"))
Y1 = int(input("Введите значение y точки 1"))
X2 = int(input("Введите значение x точки 2"))
Y2 = int(input("Введите значение y точки 1"))
A = Y1 - Y2
B = X2 - X1
C = X1 * Y2 - X2 * Y1

print (A,'*X + ', B, '*Y + ', C, "=0")
