# 1. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# not(x or y or z) == not x and not y and not z



def Check(x, y, z):
    result = not(x or y or z)
    print(f'x = {x}, y = {y}, z = {z}')
    print(result)
    None

Check (True, True, True)
Check (False, True, True)
Check (False, False, True)
Check (False, False, False)
