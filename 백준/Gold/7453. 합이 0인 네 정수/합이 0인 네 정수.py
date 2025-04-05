import sys
from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    left = []
    right = []
    
    for i in range(n):
        a, b, c, d = map(int, sys.stdin.readline().split())
        left.append((a, b))
        right.append((c, d))

    left_dict = defaultdict(int)
    left_dict = defaultdict(int)
    for i in range(n):
        for j in range(n):
            left_dict[left[i][0] + left[j][1]] += 1

    result = 0
    for i in range(n):
        for j in range(n):
            temp = (right[i][0] + right[j][1]) * -1
            if temp in left_dict.keys():
                result += left_dict[temp]
        
    print(result)