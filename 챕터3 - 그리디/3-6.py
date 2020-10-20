#  이것이 코딩테스트다 WITH 파이썬
import sys

# (강의 문제) 3-6.py => 모험가 길드 풀기
n = int(input())
arr = list(map(int,input().split()))

arr.sort() # 공포도가 낮은 인원부터 그룹

group_cnt = 0
member_cnt = 0 

for p in arr:
    member_cnt += 1
    if member_cnt >= p:
        group_cnt += 1
        member_cnt = 0

print(group_cnt)
    