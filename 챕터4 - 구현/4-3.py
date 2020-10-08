#  이것이 코딩테스트다 WITH 파이썬
import time
import sys

# 4-3.py 게임개발(시뮬레이션)
n, m = map(int, input().split())
x, y, direct = map(int, input().split())

arr = []

for i in range(m):
  arr.append(list(map(int, input().split())))

start = time.time()  # 시작 시간 저장a

# 방문 체크 배열
c_arr = [[0] * m for _ in range(n)]

# 현재 위치 방문 처리
cnt = 1
c_arr[x][y] = 1

# 다음 좌표 배열
dx_arr = [-1, 0, 1, 0]
dy_arr = [0, 1, 0, -1]

# 방향 체크
dir_check = 0

def turn_left():
  global direct

  direct -= 1
  if direct == -1:
    direct = 3


while True:
  # 회전
  turn_left()

  nx = x + dx_arr[direct]
  ny = y + dy_arr[direct]
  
  # 정면이 갈 수 있을 때
  if c_arr[nx][ny] == 0 and arr[nx][ny] == 0:
    c_arr[nx][ny] = 1
    x = nx
    y = ny
    cnt += 1
    dir_check = 0
  else:
    dir_check += 1

  # 갈 곳 없을 때
  if dir_check == 4:
    nx = x - dx_arr[direct]
    ny = y - dy_arr[direct]

    # 뒤로 이동
    if arr[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤로 이동 불가 시 시뮬레이션 종료
    else:
      break 

    dir_check = 0



print(cnt)

# 방문한 칸수 출력
print("작업시간 :", time.time() - start)
