N = int(input())
A = list(map(int, input().split()))

max_num = -100000 #最大値を格納する変数を初期化
min_num = 100000 #最小値を格納する変数を初期化

for i in range(N):
    if A[i] > max_num:
        max_num = A[i]
    if A[i] < min_num:
        min_num = A[i]

print(max_num - min_num)

# 解説
"""
1つ1つ調べるのではなく、最大値と最小値を求めてその差を取れば良い
"""