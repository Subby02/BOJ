# https://www.acmicpc.net/problem/14916

# DP (이 방법으로 품 , 비효율적인거 같음)
import sys

n = int(sys.stdin.readline())

dp = [(1e9)] * 100005

dp[0] = 0
for i in range(n+1):
  dp[i+2] = min(dp[i] + 1 , dp[i+2])
  dp[i+5] = min(dp[i] + 1 , dp[i+5])

if dp[n] == 1e9:
  print(-1)
else:
  print(dp[n])

# Greedy (다른 코드)
import sys

n = int(sys.stdin.readline())

cnt = 0
while n > 0:
  if n % 5 == 0:
    cnt += n//5
    break
  else:
    n -= 2
    cnt += 1

if n < 0:
  print(-1)
else:
  print(cnt)