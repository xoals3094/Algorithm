import sys

n, k = map(lambda x: int(x), sys.stdin.readline().strip().split())

coins = []
for _ in range(n):
    coin = int(sys.stdin.readline().strip())
    coins.append(coin)

result = 0
for i in range(1, n + 1):
    coin = coins[-i]
    if k / coin > 0:
        result += k // coin
        k %= coin

print(result)
