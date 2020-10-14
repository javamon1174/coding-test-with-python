#  이것이 코딩테스트다 WITH 파이썬
import sys

# 8-2.py => 1로 만들기 => 틀림

x = 26
# x = int(input())
operate = 0

def get_min_operate_cnt(x, operate):

    if x % 5 == 0:
        x /= 5
        operate +=1
    elif x % 3 == 0:
        x /= 3
        operate +=1
    elif x % 2 == 0:
        x /= 2
        operate +=1
    elif x == 1:
        return x
    else:
        x -= 1
        operate +=1


print("operate", operate)