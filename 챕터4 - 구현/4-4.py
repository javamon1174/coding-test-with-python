#  이것이 코딩테스트다 WITH 파이썬
import sys

# CHAPTER 04 구현 => 문자열 재정렬(4-4.py)
arr = list(map(str, input()))
# arr = 'K1KA5CB7'
# arr = 'AJKDLSI412K4JSJ9D'

string = []
integer = []
result = []

for d in arr:
    if ord(d) >= 65:
        string.append(ord(d))
    else:
        integer.append(int(d))

string.sort()

for s in string:
    result.append(chr(s))

result.append(str(sum(integer)))

print(''.join(result))
