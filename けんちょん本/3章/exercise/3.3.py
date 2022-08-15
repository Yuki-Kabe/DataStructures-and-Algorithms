N = int(input())
A = list(map(int, input().split()))

worst_value = 1000000 # 最小値を格納する変数
second_value = 1000000 # 2番目の小さい数を格納する変数
for i in range(N):
    if A[i] < worst_value: # 最小値の更新
        second_value = worst_value 
        worst_value = A[i]
    elif A[i] < second_value: # 2番目に小さい値だけの更新
        second_value = A[i]

print(second_value)

# 解説
"""
先頭から順に調べていく。
worst_valueよりも小さい値を見つけた時点でworst_valueの値は2番目に小さい数になるので、second_valueにworst_valueの値を代入し、worst_valueを更新する
worst_value < A[i] < second_value となる場合 (2番目に小さい値だけの更新) もあるのでその場合の処理も忘れずに
"""
