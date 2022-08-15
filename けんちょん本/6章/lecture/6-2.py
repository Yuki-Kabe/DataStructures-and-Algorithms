# 一般化した二分探索法の基本形(疑似コードのみ)

# x が条件を満たすかどうか
def P(x):
    if x is True:
        return True
    else:
        return False

# P(x) = True となる最小の整数 x を返す
def binary_search(x):
    left = 0 # P(left) = False となるように
    right = 100 # P(right) = True となるように

    while right - left > 1:
        mid = left + (left -right) / 2
        if P(mid):
            right = mid
        else:
            left = mid
    
    return right

