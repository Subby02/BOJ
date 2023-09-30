# https://www.acmicpc.net/problem/1085

import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(x - 0, w - x, y - 0, h - y))
