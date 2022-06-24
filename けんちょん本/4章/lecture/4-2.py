# 1からNまでの総和を計算する再帰関数の再帰呼び出しの様子

# スタックオーバーフロー対策
import sys
sys.setrecursionlimit(10**6)

def func(N):
    # 再帰関数を呼び出したことを報告する
    print("func({})を呼び出しました".format(N))

    # ベースケース
    if N == 0:
        return 0

    # 再帰的に答えを求めて出力する
    result = N + func(N-1)
    print("{}までの和 : {}".format(N, result))
    return result
     
func(5)
