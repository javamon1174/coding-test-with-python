#  이것이 코딩테스트다 WITH 파이썬
import time
import sys
from collections import deque


# 5-4.py 미로탈출
n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input())))

c_arr = [[1] * m for _ in range(n)]

# 네 방향
x_n_arr = [1, -1, 0, 0]
y_n_arr = [0, 0, 1, -1]

# 길찾기
def walking(graph, x, y, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            n_x, n_y = x + x_n_arr[i], y + y_n_arr[i]
            # 범위 초과 시 제외
            if n_x < 0 or n_x >= n or n_y < 0 or n_y >= m:
                continue
            # 괴물 있는 부분 => 0 제외
            if graph[n_x][n_y] == 0:
                continue
            # 방문 처리 후 해당 좌표 큐 삽입
            if visited[n_x][n_y] == 1:
                visited[n_x][n_y] = 0
                graph[n_x][n_y] = graph[x][y] + 1
                queue.append((n_x, n_y))

    return graph[n-1][m-1]

res = walking(arr, 0, 0, c_arr)
print(res)