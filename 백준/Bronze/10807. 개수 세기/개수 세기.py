n = int(input())
integer_list = map(int, input().split())
v = int(input())

result = 0
for integer in integer_list:
    if integer == v:
        result += 1

print(result)
