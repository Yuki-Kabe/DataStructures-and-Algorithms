# 2分探索法を用いて、「ペア和を最適化する問題」に対する全探索解放を高速化する

# upper_bound(), lower_bound()のpython版ライブラリ
import bisect

N, K = map(int, input().split())
INF = 10**10 # 十分大きな値に
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 暫定最小値を格納する変数
min_value = INF

# b をソート
b.sort()

# b に無限大を表す値(INF)を追加しておく
# これを行うことで
b.append(INF)

# aを固定して解く
for i in range(N):
    # b の中で K - a[i] 以上の範囲での最小値
    val_idx = bisect.bisect_left(b, K - a[i])
    
    # 値を取り出す
    val = b[val_idx]

    # min_value と比較する
    if a[i] + val < min_value:
        min_value = a[i] + val

print(min_value)

# 解説
"""
bisect_left について
Python ではstd::lower_bound()の代わりに bisect_left() を使用する
std::upper_bound()の代わりは bisect_right() を使用する
ソート済み配列 a と、数値 key について、a[i] ≧ key となる最小の i を返す

(ex)
a = [3,8,11,11,18,27,31]
key = 11 のとき、
bisect_left(a,key) = 2 となる

"""