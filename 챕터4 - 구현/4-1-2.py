#  이것이 코딩테스트다 WITH 파이썬
import time

print('')
# 4-1.py 시각
n = int(input()) + 1

start = time.time()  # 시작 시간 저장
cnt = 0

for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h)+str(m)+str(s):
        cnt += 1

print(cnt)

print("작업시간 :", time.time() - start)