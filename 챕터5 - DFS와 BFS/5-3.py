#  이것이 코딩테스트다 WITH 파이썬
import time
import sys

# 5-3.py 음료수 얼려 먹기 => easy
n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input())))

c_arr = [[0] * m for _ in range(n)]

# 음료수 채우기
def fill_drink(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if arr[x][y] == 1 or c_arr[x][y] == 1:
        return False

    c_arr[x][y] = 1
    
    fill_drink(x-1, y)
    fill_drink(x+1, y)
    fill_drink(x, y-1)
    fill_drink(x, y+1)

    return True

cnt = 0
for a in range(n):
    for b in range(m):
        if fill_drink(a, b):
            cnt += 1
print(cnt)
