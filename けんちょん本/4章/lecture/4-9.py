# 部分和問題を再帰関数を用いる全探索で解く

N, W = map(int, input().split())
a = list(map(int, input().split()))

def func(i, w, a):
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
func(4, 14)を呼び出すと再帰的にfunc(3,14), func(2,14), func(1,14), func(0,14)と続いて呼び出される
func(0,14) = False であるから、func(1,14)に戻り、func(0,11)が呼び出される。
func(0,11) = False であるから、func(2,14)に戻り、今度はa[i-1]を選ぶ場合、つまりfunc(1,12)が呼び出される。
ここでfunc(1,12)はfunc(0,12)を呼び出す。
func(0,12)はFalseであるから func(1,12)に戻り、a[i-1]を選ぶ場合の func(0,9)が呼び出される。
これを全ての組み合わせについて行う
"""

#動作確認用
"""
4 14
3 2 6 5
"""