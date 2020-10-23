#  이것이 코딩테스트다 WITH 파이썬
import sys

# 챕터8 다이나믹 프로그래밍 => 효율적인 화폐구성(최소한의 화폐개수 구하기)
n, m = map(int, input().split())

d = [10001] * (m+1)
money = [10001] * (n+1)

for i in range(n):
    money[i] = int(input())

d[0] = 0
for i in range(n):
    for j in range(money[i], m + 1):
        # 업데이트 방식
        d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
    print('실패')
else:
    print('최소 화폐 개수 :', d[m])
