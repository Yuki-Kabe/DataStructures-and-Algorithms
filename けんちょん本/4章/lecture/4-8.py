# フィボナッチ数列を求める再帰関数をメモ化

# メモを用意(計算していない箇所を-1で表す)
memo = [-1 for _ in range(50)]

def fibo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # メモをチェック
    if memo[N] != -1:
        return memo[N]
    
    # 答えをメモしながら、再帰呼び出し
    memo[N] = fibo(N-1) + fibo(N-2) #配列にアクセスするときに関数がよばれる
    return memo[N]

# fibo(49)を呼び出す
fibo(49)

# memo[2], memo[3], ... , memo[49]に答えが格納されている
for i in range(2, 50):
    print("{} 項目 : {}".format(i, memo[i]))