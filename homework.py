#Задание 1
"""
var1 = input()
print(var1)
"""

#Задание 2
"""
sec = int(input())
min, sec = divmod(sec, 60)
hours, min = divmod(min, 60)
print(f'{hours:d}:{min:02d}:{sec:02d}')
"""

#Задание 3
"""
num1 = int(input())
print(num1 + num1 * 11 + num1 * 111)
"""

#Задание 4
"""
large_num = int(input())
max = 1
while large_num // 10 > 0:
    print(large_num)
    if max < large_num % 10:
        max = large_num % 10
    large_num = large_num // 10
print(max)
"""

#Задание 5
"""
profit, costs = input().split()
profit = float(profit)
costs = float(costs)
print(profit, costs)
if profit > costs:
    print('Мы в плюсе')
    rent = (profit / costs)
    crew = int(input())
    eff = (rent / crew)
    print(eff)
else: print('Мы в дерьме')
"""

#Задание 6
"""
km_start, km_end = input().split()
km_start = float(km_start)
km_end = float(km_end)
period = 1
while km_end > km_start:
    km_start = (km_start + km_start * 0.1)
    print(km_start)
    period = (period + 1)
print(period)
"""