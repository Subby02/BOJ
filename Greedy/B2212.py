# https://www.acmicpc.net/problem/2212

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

array = list(set(map(int,input().split())))

diff = []
array.sort()
for i in range(len(array)-1):
  diff.append(array[i+1]-array[i])

diff.sort(reverse=True)

print(sum(diff[k-1:]))