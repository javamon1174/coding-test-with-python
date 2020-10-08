#  이것이 코딩테스트다 WITH 파이썬
import time

# 3-4.py 1이 될 때까지
n, k= map( int, input().split())

cnt = 0
start = time.time()  # 시작 시간 저장

while True:
    if n == 1:
        break
    elif n % k == 0:
        n = int(n/k)
    else:
        n = n - 1

    cnt += 1

print(cnt)
print("작업시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

count = 0;
start = time.time()  # 시작 시간 저장
# 다른 형태도 알아 두기
while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1

while n != 1:
    n -= 1
    count += 1

print(count)

print("작업시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간