# フィボナッチ数列を求める再帰関数の再帰呼び出しの様子

def fibo(N):
    # 再帰関数を呼び出したことを報告する
    print("fibo({}) を呼び出しました".format(N))

    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # 再帰的に答えを求めて出力する
    result = fibo(N-1) + fibo(N-2)
    print("{} 項目 = {}".format(N, result))
    return result

fibo(6)