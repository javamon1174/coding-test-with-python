#  이것이 코딩테스트다 WITH 파이썬

# 6-2.py 위에서 아래로
n = int(input())
arr = [None] * n

for i in range(n):
    arr[i] = int(input())

'''
arr.sort()
print(arr[::-1])
'''

arr = sorted(arr, reverse = True)
print(arr)
