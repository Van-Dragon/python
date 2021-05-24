#Task 1 Done
"""
my_list = ['word', 123, 45.6, 'another word']
print(my_list)
print(type(my_list))
print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))
print(type(my_list[3]))
"""

#Task 2 - не смог разобраться с переменой индексов в списках до конца
"""
example_list = ['Tiefe', 'Wasser', 'Sind', 'Nicht']
print(example_list)
print(example_list[::2])
print(example_list[1::2])
final_list = example_list[::2], example_list[1::2] = example_list[1::2], example_list[::2]
print(final_list)
"""

#Task 3.1 Done
"""
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
month = int(input('Введите месяц в виде целого числа\n'))
for el in winter:
    if month == el:
        print('winter')
for el in spring:
    if month == el:
        print('spring')
for el in summer:
    if month == el:
        print('summer')
for el in fall:
    if month == el:
        print('fall')
"""

#Task 3.2 Done
"""
year = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'fall': [9, 10, 11]}
month = int(input('Введите месяц в виде целого числа\n'))
for key, value in year.items():
    if month in value:
        print(month, key)
"""

#Task 4 Done
"""
user_list = list((input('Введите текст\n').split(" ")))
for ind, el in enumerate(user_list, 1):
    print(ind, el[:10])
"""

#Task 5 Done
"""
rate_list = [7, 5, 3, 3, 2]
print(rate_list)
rate_list.append(int(input('Введите целое число\n')))
rate_list.sort(reverse=True)
print(rate_list)
"""
