#  이것이 코딩테스트다 WITH 파이썬
import time

print('')
# 4-2.py 왕실의 나이트
n = str(input())
row = int(n[1])
col = int(ord(n[0])) - int(ord('a'))+1


start = time.time()  # 시작 시간 저장
cnt = 0

# 8가지 경우의 수
case = [(2, 1), (1, 2), (-2, 1), (-1, 2), (1, -2), (2, -1), (-2, -1), (-1, -2)]

for ca in case:
  r, c = ca

  n_r = row + r
  n_c = col + c

  if n_r > 0 and n_r <= 8 and n_c > 0 and n_c <= 8:
    cnt += 1

print("경우의 수 : ", cnt)

print("작업시간 :", time.time() - start)
