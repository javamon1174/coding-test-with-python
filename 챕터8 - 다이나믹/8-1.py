#  이것이 코딩테스트다 WITH 파이썬
import sys

# CHAPTER 08 다이나믹 프로그래밍 => 피보나치 수열
d = [0] * 100

d[1], d[2] = 1, 1

def fibo(x):
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(50))