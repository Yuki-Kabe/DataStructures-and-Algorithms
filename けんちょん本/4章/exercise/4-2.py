# トリボナッチ数列を求める再帰関数をメモ化

# メモを用意(計算していない箇所を-1で表す)
memo = [-1 for _ in range(11)]

def Tribo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    
    # メモをチェック
    if memo[N] != -1:
        return memo[N]
    
    # 答えをメモしながら、再帰呼び出し
    memo[N] = Tribo(N-1) + Tribo(N-2) + Tribo(N-3) #配列にアクセスするときに関数がよばれる
    return memo[N]

# Tribo(10)を呼び出す
Tribo(10)

# memo[3], memo[4], ... , memo[10]に答えが格納されている
for i in range(3, 11):
    print("{} 項目 : {}".format(i, memo[i]))