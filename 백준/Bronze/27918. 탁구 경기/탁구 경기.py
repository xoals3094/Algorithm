N = int(input())
D = 0
P = 0
for _ in range(N):
    if input().rstrip() == 'D':
        D += 1
    else:
        P += 1
    if abs(D - P) >= 2:
        break
        
print(f'{D}:{P}')