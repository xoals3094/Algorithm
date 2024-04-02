def is_end_number(number: int):
    return '666' in str(number)


def run():
    n = int(input(''))
    number = 666
    i = 0
    while True:
        if is_end_number(number):
            i += 1
        if i == n:
            return number
        number += 1


print(run())
