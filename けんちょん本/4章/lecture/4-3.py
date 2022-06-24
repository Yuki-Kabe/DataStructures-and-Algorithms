# 再帰呼び出しが止まらない再帰関数

def func(N):
    # ベースケース
    if N == 0:
        return 0
    
    # 再帰呼び出し(止まらなくなるので注意)
    return N + func(N+1)