# トリボナッチ数列
def Tribonacci(N):
    # ベースケース
    if N == 0:
        return 0
    if N == 1:
        return 0
    if N == 2:
        return 1
    # 再帰呼び出し
    return Tribonacci(N-1) + Tribonacci(N-2) + Tribonacci(N-3)

# 1から10まで表示
for i in range(1,11):
    print("i:{}, Tribonacci:{}".format(i, Tribonacci(i)))
