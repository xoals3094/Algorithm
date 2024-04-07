import sys

n, m = map(lambda x: int(x), sys.stdin.readline().split())

not_hear_and_see_peoples = {}
not_hear_peoples = []
for _ in range(n):
    name = sys.stdin.readline().strip()
    not_hear_and_see_peoples[name] = False
    not_hear_peoples.append(name)

not_see_peoples = []
for _ in range(m):
    name = sys.stdin.readline().strip()
    not_hear_and_see_peoples[name] = False
    not_see_peoples.append(name)


for name in not_hear_peoples:
    not_hear_and_see_peoples[name] = True

results = []
for name in not_see_peoples:
    if not_hear_and_see_peoples[name]:
        results.append(name)

results.sort()
print(len(results))
for name in results:
    print(name)