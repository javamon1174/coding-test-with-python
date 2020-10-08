#  이것이 코딩테스트다 WITH 파이썬
import time

print('')
# 4-1.py 상하좌우
n = int(input())
move = input().split()

start = time.time()  # 시작 시간 저장
row, col = 1, 1

for m in move:
  if m == 'R' and col < n:
    col += 1
  elif m == 'L' and col > 1:
    col -= 1
  elif m == 'U' and row > 1:
    row -= 1
  elif m == 'D' and row < n:
    row += 1

print(row, col)


print("작업시간 :", time.time() - start)