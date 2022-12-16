# Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21



import math

def Num_Point (num_point):
    print(f'Введите значения точки {num_point}: ')
    None

def Coor(point):
    print(f'{point}: ')
    p = int(input())
    return p

def distance(xa,ya,xb,yb):
    d = math.sqrt((xb-xa)**2+(yb-ya)**2)
    return d

Num_Point('a')
xa = Coor('x')
ya = Coor('y')

Num_Point('b')
xb = Coor('x')
yb = Coor('y')

result = round(distance(xa,ya,xb,yb), 3)
print(result)
    