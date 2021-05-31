def salary_calc(x, y, z):
    return (x * y + z)

hours, rate, bonus = map(int, input('Укажите отработанное время, ставку в час и премиальную часть: \n').split())
salary = salary_calc(hours, rate, bonus)
print(salary)