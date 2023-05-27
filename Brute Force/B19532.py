# https://www.acmicpc.net/problem/19532

# Brute Force
import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
  for y in range(-999, 1000):
    if a * x + b * y == c and d * x + e * y == f:
      print(x, y)
      break

# mathmatic
import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

x = (e * c - b * f) // (a * e - d * b)
y = (c * d - a * f) // (d * b - a * e)

print(x, y)
