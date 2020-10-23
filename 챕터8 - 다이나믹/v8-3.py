#  이것이 코딩테스트다 WITH 파이썬
import sys

# CHAPTER 08 다이나믹 프로그래밍 => 개미전사 8-3.py
d = [0] * 100

n = int(input())
li = list(map(int, input().split()))

d[0] = li[0]
d[1] = max(li[0], li[1])

for i in range(2, n):
    # [1, 3, 1, 5]
    # d[i] = max(3, 3 + 5) => 점화식으로 풀이
    d[i] = max(d[i-1], d[i-2] + li[i])

print(d[n-1])