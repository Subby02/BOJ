# https://www.acmicpc.net/problem/20546

import sys

input = sys.stdin.readline

money = int(input())

prices = list(map(int , input().split()))

jh_money = money
jh_stock = 0
sm_money = money
sm_stock = 0

change = 0
prev_price = 0
for i in range(14):
  if change >= 0:
    if prev_price < prices[i]:
      change += 1
    elif prev_price > prices[i]:
      change = -1
  else:
    if prev_price < prices[i]:
      change = 1
    elif prev_price > prices[i]:
      change -= 1
  
  if change <= -3:
    if sm_money // prices[i] >= 1:
      sm_stock += sm_money // prices[i]
      sm_money %= prices[i]
  elif change >= 3:
    if sm_stock > 0:
      sm_money += prices[i] * sm_stock
      sm_stock = 0
      
  prev_price = prices[i]

  
  if jh_money // prices[i] >= 1:
    jh_stock += jh_money // prices[i]
    jh_money %= prices[i]

  
jh_money = jh_stock*prices[-1] + jh_money
sm_money = sm_stock*prices[-1] + sm_money

if jh_money > sm_money:
  print('BNP')
elif jh_money < sm_money:
  print('TIMING')
else:
  print('SAMESAME')
    
  