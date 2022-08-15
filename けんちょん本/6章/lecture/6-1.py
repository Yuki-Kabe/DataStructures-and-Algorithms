# 配列から目的の値を探索する二分探索法

N = 8
a = [3,5,8,10,14,17,21,39]

# 目的の値 key の添字を返す (存在しない場合は -1を返す)
def binary_search(key):
    left = 0 # 配列 a の左端
    right = len(a) - 1 # 配列 a の右端
    while left <= right:
        mid = left + (right - left) // 2 # 区間の真ん中
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            right = mid -1
        elif a[mid] < key:
            left = mid + 1
    else:
        return -1
    
print(binary_search(10)) # 3
print(binary_search(3)) # 0
print(binary_search(39)) # 7

print(binary_search(-100)) # -1
print(binary_search(9)) # -1
print(binary_search(100)) # -1


# 解説
"""
やっていることは単純で
区間の真ん中の値(a[mid]) と key が一致するか,探索する区間の幅が0になるまでループを繰り返す
真ん中の値に一致しない場合はkeyの値によって真ん中より右側か左側を調べるように区間の端のインデックスを変化させる

while文の条件として right >= left となっているが、
これは調べる区間が1以上のとき という状態を表している
要素数が1のときの処理を考える
このとき、right = left となっている
mid = left + (right - left) // 2 = left + (left - left) = left
a[mid] == keyでなければ
right = mid - 1 = left - 1 か left = mid + 1 = left + 1 となり、
left <= right を満たさないのでループが終了する

a[mid] と keyを比較する部分について
a[mid] == key であったら midを返す
key < a[mid]  の場合、keyは2つに分けた左側のグループに属するので、調べる区間の右端を移動させる
次の探索はmidから左側の区間、つまりindexで言うとleft から mid-1 の区間について探索する
a[mid] < key  の場合、keyは2つに分けた右側のグループに属するので、調べる区間の左端を移動させる
次の探索はmidから右側の区間、つまりindexで言うとmid+1 から right の区間について探索する
"""