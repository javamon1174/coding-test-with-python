# 3-3.py 숫자 카드 게임
n, m = map(int, input().split())

res = 0
for i in range(n):
  row = list(map(int,input().split()))
  if res < min(row):
    res = min(row)
  
print(res)
