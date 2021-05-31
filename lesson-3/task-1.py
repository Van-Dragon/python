def my_divide():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    if num2 == 0:
        return ('Не в этой математике, дитя')
    return (num1 / num2)

result = my_divide()
print(result)

#Done