N = int(input())
if N == 0:
    print(1)
else:
    result = 1
    for x in range(1, N + 1):
        result *= x
    print(result)