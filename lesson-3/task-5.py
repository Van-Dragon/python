def special_sum(data):
    check = sum(data)
    return check

def special_filter(x):
    return x > 3

data = [1, 2, 3, 4, 5]
print(list(filter(special_filter, data)))

result = list(special_sum)
print(result)