import sys

N = int(sys.stdin.readline().strip())


def get_prime_numbers(n):
    arr = [True for _ in range(n + 1)]
    for x in range(2, n + 1):
        if not arr[x]:
            continue

        i = 2
        while x * i <= n:
            arr[x * i] = False
            i += 1

    prime_numbers = []
    for x in range(2, n + 1):
        if arr[x]:
            prime_numbers.append(x)
    return prime_numbers


def prime_sum_cases(n):
    prime_numbers = get_prime_numbers(n)
    start = 0
    end = 0
    total = prime_numbers[0] if len(prime_numbers) > 0 else 0
    count = 0
    while end < len(prime_numbers) - 1:
        if total == n:
            count += 1

        if total <= n or start == end:
            end += 1
            total += prime_numbers[end]

        elif total > n:
            total -= prime_numbers[start]
            start += 1

    while start < len(prime_numbers):
        if total == n:
            count += 1

        total -= prime_numbers[start]
        start += 1

    return count

print(prime_sum_cases(N))
