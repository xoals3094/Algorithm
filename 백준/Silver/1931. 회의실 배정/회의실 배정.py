import sys

MAX = 2_147_483_647


class Conference:
    def __init__(self, start, end):
        self.start = start
        self.end = end


N = int(sys.stdin.readline().strip())

conferences = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    conferences.append(Conference(start, end))

conferences.sort(key=lambda x: (x.end, x.start))


count = 0
selected_conference = Conference(0, 0)
for conference in conferences:
    if conference.start < selected_conference.end:
        continue

    count += 1
    selected_conference = conference

print(count)

