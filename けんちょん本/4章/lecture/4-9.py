# 部分和問題を再帰関数を用いる全探索で解く

N, W = map(int, input().split())
a = list(map(int, input().split()))

def func(i, w, a): # 配列a の中から i個選んで　wを作ることができるか
    # ベースケース
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    # 再帰呼び出し
    if func(i-1, w, a): # a[i-1]を選ばない場合
        return True
    if func(i-1, w-a[i-1], a): # a[i-1]を選ぶ場合
        return True
    
    # どちらもFalseの場合はFalse
    return False

if func(N, W, a):
    print("Yes")
else:
    print("No")

# 解説
"""
p54のように関数を呼び出すと上から下に降りていくイメージ
ベースケースは一番下の段にたどり着いた場合の判定 (ベースケースになるまで呼び出して結果が得られたら1つ上の段に戻る)
func(4, 14, a)を呼び出すと再帰的にfunc(3,14,a), func(2,14,a), func(1,14,a), func(0,14,a)と続いて呼び出される
func(0,14,a) = False であるから、func(1,14,a)に戻り、今度はa[i-1]を使う場合のfunc(0,11,a)が呼び出される。
func(0,11,a) = False であるから、func(2,14,a)に戻り、a[i-1]を選ぶ場合、つまりfunc(1,12,a)が呼び出される。
ここでfunc(1,12,a)はfunc(0,12,a)を呼び出す。
func(0,12,a)はFalseであるから func(1,12,a)に戻り、a[i-1]を選ぶ場合の func(0,9,a)が呼び出される。
これを全ての組み合わせについて行う
"""

#動作確認用
"""
4 14
3 2 6 5
"""