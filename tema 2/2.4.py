num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Деление на ноль невозможно"

print("Сложение:", addition)
print("Вычитание:", subtraction)
print("Умножение:", multiplication)
print("Деление:", division)
