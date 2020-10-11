#  이것이 코딩테스트다 WITH 파이썬
import sys
# 7-2.py => 부품 찾기

# 이진탐색 - 재귀
def b_search(arr, t, start, end):
    if start > end:
        return print('no', end=' ')
    
    mid = int((start+end)// 2)

    if arr[mid] == t:
        return print('yes', end=' ')

    if t > mid:
        b_search(arr, t, mid+1, end)
    else:
        b_search(arr, t, start, mid-1)

# 입력부 * sys.stdin.readline().rstrip()

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 초기화
n_list.sort()

for target in m_list:
    b_search(n_list, target, 0, len(n_list)-1)

print(' ')