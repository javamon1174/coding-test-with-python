#  이것이 코딩테스트다 WITH 파이썬
import sys

# 챕터8 다이나믹 프로그래밍 => 1로 만들기
n = int(input())
res = [0] * 30001

for i in range(2, n+1):
    res[i] = res[i - 1] + 1

    # 업데이트 방식(보텀업))
    if i % 2 == 0: # 인덱스를 매개로 나머지가 0일 경우
        res[i] = min(res[i], res[i // 2] + 1)
    if i % 3 == 0:
        res[i] = min(res[i], res[i // 3] + 1)
    if i % 5 == 0:
        res[i] = min(res[i], res[i // 5] + 1)

print(res[n])