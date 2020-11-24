#  이것이 코딩테스트다 WITH 파이썬
import sys

# 10-3 문제 - 도시 분할 계획

# 부모테이블 전역 변수 선언
parent = []


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def work():
    v, e = list(map(int, input().split(' '))) # 팀 수, 연산 수 입력 받기
    parent = [0] * (v + 1) # 부모 테이블 초기화

    edges = [
        (3, 1, 2),
        (2, 1, 3),
        (1, 3, 2),
        (2, 2, 5),
        (4, 3, 4),
        (6, 7, 3),
        (5, 5, 1),
        (2, 1, 6),
        (1, 6, 4),
        (3, 6, 5),
        (3, 4, 5),
        (4, 6, 7),
    ]
    result = 0

    for i in range(1, v+1):
        parent[i] = i

    edges.sort()
    last = 0

    for edge in edges:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            last = cost
    
    print('result', result, 'last', last)
    print(result - last)



work()
