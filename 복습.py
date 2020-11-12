# 복습은 함수형으로 구현
def training_1(): # 거스름돈
    n = 1260
    cnt = 0

    for c in [500, 100, 50, 10]:
        cnt += n // c
        n %= c

    print('거스름돈 개수 :', cnt)

def training_2(): # 1이 될떄까지
    n = 16
    k = 4
    cnt = 0

    while n >= k: #
        while n % k != 0: # 나누어 질때까지 1씩 빼기
            n -= 1
            cnt += 1

        n //= k
        cnt += 1

    cnt += n - 1

    print('연산 횟수 :', cnt)


def training_3(): # 1이 될떄까지 log n 시간 복잡도 형태
    n = 17
    k = 7
    cnt = 0

    while True:
        # n이 k로 나누어 떨어지는 수가 될떄까지 빼기
        t = (n // k) * k
        cnt += n - t
        n = t

        # 나눌 수 없을 때 탈출
        if n < k:
            break
        
        cnt += 1
        n //= k

    cnt += n - 1

    print('연산 횟수 :', cnt)

def training_3(): # 1이 될떄까지 log n 시간 복잡도 형태
    n = 17
    k = 7
    cnt = 0

    while True:
        # n이 k로 나누어 떨어지는 수가 될떄까지 빼기
        t = (n // k) * k
        cnt += n - t
        n = t

        # 나눌 수 없을 때 탈출
        if n < k:
            break
        
        cnt += 1
        n //= k

    cnt += n - 1

    print('연산 횟수 :', cnt)

