# フィボナッチ数列を求める再帰関数

def fibo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # 再帰呼び出し
    return fibo(N-1) + fibo(N-2)

print(fibo(10)) # 55