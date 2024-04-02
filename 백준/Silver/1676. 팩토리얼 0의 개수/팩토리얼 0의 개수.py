def factorial(n: int):
    result = 1
    for x in range(1, n + 1):
        result *= x

    return result


def count_zero(d: int):
    d = str(d)
    i = 1
    while True:
        if d[-i] == '0':
            i += 1
            continue
        return i - 1


def run():
    n = int(input(''))
    d = factorial(n)
    print(count_zero(d))


run()
