def example(first):
    result = []
    for i in first:
        if i not in result:
            result.append(i)
    return result

first = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(result)