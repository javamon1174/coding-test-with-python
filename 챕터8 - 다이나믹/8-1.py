#  이것이 코딩테스트다 WITH 파이썬
import sys

# CHAPTER 08 다이나믹 프로그래밍 => 피보나치 수열
# 탑 다운(재귀함수)
d = [0] * 100

d[1], d[2] = 1, 1

def fibo(x):
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(50))

# 보텀업(반복문)
e = [0] * 100

e[1], e[2], n = 1, 1, 50

for i in range(3, n+1):
    e[i] = e[i-1] + e[i-2]

print(e[n])