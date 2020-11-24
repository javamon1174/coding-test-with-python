#  이것이 코딩테스트다 WITH 파이썬
import sys


# 부모테이블 전역변수 선언
parent = []


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 10-2 문제 - 팀결성
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def work():
    n, m = list(map(int, input().split(' '))) # 팀 수, 연산 수 입력 받기
    parent = [0] * (n + 1) # 부모 테이블 초기화

    # 모든 부모 자기 자신으로 초기화
    for i in range(0, n + 1):
        parent[i] = i 

    # 연산 반복문
    for i in range(m):
        oper, a, b= list(map(int, input().split(' '))) # 팀 수, 연산 수 입력 받기
        # oper == 0 => 팀 합치기 / oper == 1 => 팀 여부 확인
        if oper == 0:
            union_parent(parent, a, b)
        elif oper == 1:
            if find_parent(parent, a) == find_parent(parent, b):
                print('YES')
            else:
                print('NO')

work()
