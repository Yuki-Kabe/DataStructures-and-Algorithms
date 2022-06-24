# ユークリッドの互除法によって最大公約数を求める

def gcd(x,y):
    # yがxより大きいときは入れ替える
    if x < y: 
        x,y = y,x
    
    # ベースケース
    if y == 0: 
        return x
    
    # 再帰呼び出し
    return gcd(y, x%y)


print(gcd(10,30))

# 解説
"""
gcd(10,30)のとき(x < yのとき)も対応できるようにした
"""