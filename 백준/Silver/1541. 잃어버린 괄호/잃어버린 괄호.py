import sys

split_minus_list = sys.stdin.readline().strip().split('-')
numbers = []
for split_minus in split_minus_list:
    number = 0
    for a in split_minus.split('+'):
        number += int(a)
    numbers.append(number)

result = numbers[0]
for number in numbers[1:]:
    result -= number

print(result)
