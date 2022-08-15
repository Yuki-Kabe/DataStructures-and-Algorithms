# コイン問題を解く貪欲法

# コインの金額
value = [500, 100, 50, 10, 5, 1]

# 入力
X = int(input())
a = list(map(int, input().split()))

# 貪欲法
result = 0
for i in range(6):
    # 枚数制限がない場合の枚数
    add = X // value[i]

    # 枚数制限を考慮
    if add > a[i]:
        add = a[i]
    
    # 残り金額を求めて、答えに枚数を加算する
    X -= add * value[i]
    result += add

print(result)