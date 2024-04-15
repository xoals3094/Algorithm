n = []
for _ in range(28):
    n.append(int(input()))

n.sort()

not_submit = []
for x in range(1, 30 + 1):
    if x not in n:
        not_submit.append(x)

for member in not_submit:
    print(member)

