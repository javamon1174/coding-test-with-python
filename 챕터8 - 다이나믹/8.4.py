#  이것이 코딩테스트다 WITH 파이썬
import sys

# 챕터8 다이나믹 프로그래밍 => 바닥공사
n = int(input())

# 경우의수 배열
res = [0] * 1001
res[1] = 1 # 경우의 수 1가지 => 1x2
res[2] = 3 # res[1] + 경우의 수 2가지 => a) 2x1 * 2  b) 2x2 

for i in range(3, n+1):
    # 왼쪽부터 경우의 수를 누적 => 곱하기 2는 경우의 수 두가지가 누적되기 떄문
    res[i] = res[i-1] + (2 * res[i-2]) % 796796

print(res[n])
