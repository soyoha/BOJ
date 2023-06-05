import collections
import sys

input = sys.stdin.readline
N, L = map(int, input().split())
A = list(map(int, input().split()))
prevs = collections.deque()
results = []

for i, cur in enumerate(A):
    while prevs and prevs[0][0] <= i - L:
        prevs.popleft()
    while prevs and prevs[-1][1] >= cur:
        prevs.pop()

    prevs.append((i, cur))

    results.append(prevs[0][1])

print(*results)
