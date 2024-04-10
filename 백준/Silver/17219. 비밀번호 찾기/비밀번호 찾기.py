import sys


class Memo:
    def __init__(self, url, pw):
        self.url = url
        self.pw = pw


n, m = map(lambda x: int(x), sys.stdin.readline().strip().split())

memos = []
for _ in range(n):
    url, pw = sys.stdin.readline().strip().split()
    memo = Memo(url, pw)
    memos.append(memo)

memos.sort(key=lambda x: x.url)


def find_pw(url):
    start = 0
    end = n - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if url < memos[mid].url:
            end = mid
        elif url > memos[mid].url:
            start = mid
        elif url == memos[mid].url:
            return memos[mid]

    if memos[start].url == url:
        return memos[start]
    return memos[end]


for _ in range(m):
    url = sys.stdin.readline().strip()
    memo = find_pw(url)
    print(memo.pw)