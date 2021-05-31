"""
def exp():
    num1 = float(input('Введите положительное число: '))
    num2 = int(input('Введие целое отрицательное число: '))
    return num1 ** num2

result = exp()
print(result)
"""

def exp():
    num1 = float(input('Введите положительное число: '))
    x = num1
    num2 = int(input('Введие целое отрицательное число: '))
    while num2 < -1:
        num1 = (num1 * x)
        num2 = (num2 + 1)
    return (1 / num1)

result = exp()
print(result)

#Done