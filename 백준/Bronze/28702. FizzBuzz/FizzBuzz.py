import sys

fb = []

for _ in range(3):
    fb.append(sys.stdin.readline().strip())

for i, value in enumerate(fb):
    try:
        int(value)
    except Exception:
        continue

    fizzbuzz = (int(value) + (3 - i))
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        fizzbuzz = 'FizzBuzz'

    elif fizzbuzz % 3 == 0:
        fizzbuzz = 'Fizz'

    elif fizzbuzz % 5 == 0:
        fizzbuzz = 'Buzz'
    print(fizzbuzz)
    break
