import string

r = 31
M = 1234567891


def convert(alphabet: str):
    return string.ascii_lowercase.index(alphabet) + 1


def element(a: int, i: int):
    return a*(r**i)


def main():
    L = int(input(''))
    s = input('')

    result = 0
    for i in range(L):
        a = convert(s[i])
        result += element(a, i)

    print(result % M)

main()