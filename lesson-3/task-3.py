def my_func():
    var1, var2, var3 = (int(i) for i in input('Введите 3 числа через пробел: ').split())
    x = (var1 + var2 + var3) - min(var1, var2, var3)
    return x

result = my_func()
print(result)

#Done