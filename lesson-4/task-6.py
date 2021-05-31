from itertools import cycle
from itertools import count
"""
gen = int(input())
for el in count(1, 1):
    if el > 30:
        break
    print(el)
    gen += 1
"""

gen = 1
for el in cycle('1234'):
    if gen > 30:
        break
    print(el)
    gen += 1