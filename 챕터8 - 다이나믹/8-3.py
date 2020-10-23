#  이것이 코딩테스트다 WITH 파이썬
import sys

# 챕터8 다이나믹 프로그래밍 => 개미전사
n = int(input())
arr = list(map(int, input().split(' ')))
res = [0] * len(arr) # 결과 저장 배열

# 초기값 세팅
res[0] = arr[0]
res[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
    res[i] = max(res[i-1], res[i-2] + arr[i])

print(res[n-1])

