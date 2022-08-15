# 射撃王問題に対する2分探索法

# 入力
N = int(input())
H = []
S = []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

# 2分探索の上限値を求める
M = 0
for i in range(N):
    M = max(M, H[i] + S[i]*N)

# 2分探索
left = 0
right = M
while right - left > 1:
    mid = left + (right - left)//2
    # 判定する
    flg = True
    time = [0]*N # 各風船を割るまでの制限時間
    for i in range(N):
        # そもそも mid が 初期高度より高かったら False
        if mid < H[i]:
            flg = False
        else:
            time[i] = (mid - H[i]) // S[i]
    # 時間が差し迫っている順にソートする
    time.sort()
    
    for i in range(N):
        # 時間切れの場合は False
        if time[i] < i:
            flg = False

    if flg:
        right = mid
    else:
        left = mid

print(right)





# 解説
"""
P96の一般化した2分探索法の考えを用いる
N個の風船全てについてペナルティをx以下にできるかどうか判定する
各風船のペナルティをx以下に抑える必要があるので各風船を何秒以内に割るべきかが決まる
その時間制限が最も差し迫っているものから優先的に割っていき、全ての風船が割れればYes, 途中で高さがxを超えるような風船が現れたらNo と判定する
Yesとなるxの最小値が答え

M : 考えうる最大秒
として、[0,M]を2分探索する。
風船を割る順番について考える。
風船 i は スタートの段階で高さ H[i] にあり、毎秒 S[i] ずつ上昇していく。
ペナルティを x とすると 風船 i は高さ H[i] から 高さ x になるまでに (x-H[i])//S[i] 秒かかる
これを全ての風船について求めて、xになるまでにかかる時間が短いものから順に割っていけば良いことになる。

(x-H[i])//S[i] について
図を書いてみればわかりやすいが、具体例で考えてみる
H=10, x=20, S=2 とすれば、 Hがxに辿り着くまでにかかる時間は (20-10)//2 = 5秒

2分探索では区間[0,M]からスタートし、区間をどんどん半分にしていく
ペナルティ x = midであり、このペナルティで全ての風船が割れるようであれば、mid が小さくなるように区間を狭める(right = mid)
反対にこのペナルティで全ての風船が割れないようであれば、 mid を大きくなるように区間を狭める (left = mid)
P97に記述してある通り、rightは常にTrue側におり、leftは常にFalse側にいるので、探索が終了したらrightを出力する

"""