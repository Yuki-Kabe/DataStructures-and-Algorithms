N = int(input())
A = list(map(int, input().split()))

def how_many_times(x):
    count = 0
    while x %2 == 0: # 2で割り切れなくなるまで続ける
        x //= 2
        count += 1
    return count 

result = 10000000 # 解答を格納する変数を初期化

for i in range(N):
    if how_many_times(A[i]) < result:
        result = how_many_times(A[i])

print(result)


# 解説
"""
各a[i]を2で割り切れなくなるまで割り、割れた回数の最小値が求める答えとなる
(ex)
A = [8, 12, 16]である場合、それぞれ2で割れる回数は 3回, 2回, 4回であるから求める答えは2である
"""