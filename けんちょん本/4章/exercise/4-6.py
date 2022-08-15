# 部分和問題をメモ化再帰を用いる全探索で解く

N, W = map(int, input().split())
a = list(map(int, input().split()))

memo = [[-1]*(W+1) for _ in range(N)] # memo[i][w] : i個選んでwを作ることはできるかどうか

"""
未完成

def func(i, w, a):
    # ベースケース
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    # メモをチェック(既に計算済みなら答えをリターン)
    if memo[i][w] != -1:
        return memo[i][w]

    # 答えをメモしながら再帰呼び出し
    # a[i-1]を選ばない場合
    if func(i-1, w, a):
        memo[i][w] = 1
        return memo[i][w]
    
    # a[i-1]を選ぶ場合
    if func(i-1, w-a[i-1], a):
        memo[i][w] = 1
        return memo[i][w]


if func(N, W, a):
    print("Yes")
else:
    print("No")
"""


    
    


