# 3-2.py 큰수의 법칙
n, m, k = map(int, input().split())
arr = list(map(int,input().split()))

arr.sort()

big1 = arr[n-1]
big2 = arr[n-2]

big2_cnt = m%k
big1_cnt = m-big2_cnt

print(big1_cnt*big1 + big2_cnt*big2)