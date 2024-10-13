import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4 * a * c  

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Корни: {root1} и {root2}")
elif d == 0:
    root = -b / (2 * a)
    print(f"имеет один корень: {root}")
else:
    print("не имеет вещественных корней.")
