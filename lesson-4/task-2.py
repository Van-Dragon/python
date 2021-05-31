example = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = []
for elem, prev_elem in example:
    if elem > prev_elem:
        result.append(elem)

print(result)