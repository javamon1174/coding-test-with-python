#  이것이 코딩테스트다 WITH 파이썬

# 6-3.py => 성적이 낮은 순서로 학생 출력하기(성적 - 오름차순)
def score(data):
    return data[1]

n = int(input())
arr = []

for i in range(n):
    n, k = map(str, input().split())
    arr.append((n, int(k)))

for i in sorted(arr, key=score):
    print(i[0], end=' ')
print('')
