#  이것이 코딩테스트다 WITH 파이썬
import sys

# (강의 문제) 3-5.py => 곱하기 혹은 더하기
int_arr = list(map(int, input()))
result = int_arr[0]

for i in range(1, len(int_arr)):
    # 결과 값 또는 현재 입력 값 둘 중 하나라도 1보다 작거나 같으면 덧샘
    if result <= 1 or int_arr[i] <= 1:
        result += int_arr[i]
    else:
        result *= int_arr[i]


# (강의 문제) 3-6.py => 모험가 길드 풀기

print(result)