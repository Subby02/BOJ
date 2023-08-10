# https://www.acmicpc.net/problem/13164

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = list(map(int, input().split()))

diff = []
for i in range(1, n):
  diff.append(array[i] - array[i - 1])

diff.sort(reverse=True)

print(sum(diff[k - 1:]))
