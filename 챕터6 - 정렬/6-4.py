#  이것이 코딩테스트다 WITH 파이썬
import sys
# 6-4.py => 두 배열의 원소 교체
n, k = map( int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

''' 교재 참고 풀이
arr_a = sorted(arr_a)
arr_b = sorted(arr_b, reverse = True)

for i in range(k):
    # 두 배열 간 데이터 비교
    if arr_b[i] > arr_a[i]:
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    # A 배열이 더 클 경우 반복문 종료
    else:
        break

print(sum(arr_a))
'''

for i in range(k):
    min_idx = 0
    max_idx = 0
    min_value = 999
    max_value = 0

    for x in range(n):
        # 최소 인덱스 구하기
        if min_value > arr_a[x]:
            min_idx = x
            min_value = arr_a[x]
        # 최대 인덱스 구하기
        if max_value < arr_b[x]:
            max_idx = x
            max_value = arr_b[x]

    # 두 배열 간 값 스와핑
    arr_a[min_idx], arr_b[max_idx] = arr_b[max_idx], arr_a[min_idx]

print(sum(arr_a))
