import sys

N = int(sys.stdin.readline().strip())

s_length = int(sys.stdin.readline().strip())

S = sys.stdin.readline().strip()

i = 0
n = 0
result = 0
while i < s_length - 2:
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I':
        n += 1
        i += 2
        continue

    if n >= N:
        result += (n - N) + 1

    n = 0
    i += 1

print(result + (0 if (n - N) + 1 < 0 else (n - N) + 1))

