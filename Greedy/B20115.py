# https://www.acmicpc.net/problem/20115

import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int , input().split()))

array.sort()

total = sum(array[:-1])

print(total/2 + array[-1])
