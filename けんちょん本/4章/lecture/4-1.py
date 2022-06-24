# 1からNまでの総和を計算する再帰関数

def func(N):
    # ベースケース
    if N == 0:
        return 0
    
    # 再帰呼び出し
    return N + func(N-1)

print(func(5))