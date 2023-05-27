# https://www.acmicpc.net/problem/1010

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n,m = map(int , input().split())
  c = [[0] * (m+1) for _ in range(m+1)]
  for i in range(1,m+1):
    c[i][0] = 1
    c[i][i] = 1

  for i in range(2,m+1):
    for j in range(m+1):
      c[i][j] = c[i-1][j] + c[i-1][j-1]

  print(c[m][n])

# 아주 좋은 문제인거 같다. 파스칼 삼각형 까지 떠올렸는데 어떻게 코딩을 해야될지 몰라서 결국엔 답을 보긴 했지만 조합 까지 생각했다는 부분에서 만족한다.
# I think this problem is very good. Finally, I searched code but i could reach 'Pascal's triangle'. I'm happy that i thought of combination