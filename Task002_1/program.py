# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)



print('Введите номер плоскости(1-4): ')
space = int(input())
if space == 1: print('x > 0 and y > 0')
elif space == 2: print('x > 0 and y < 0')
elif space == 3: print('x < 0 and y < 0')
elif space == 4: print('x < 0 and y > 0')
else: print('Ошибка ввода')