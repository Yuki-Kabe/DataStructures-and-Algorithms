K, N = map(int, input().split())

count = 0
for x in range(min(N,K)+1): # K > N のときはそもそもだめなので範囲をmin(N,K)までとする
    for y in range(min(N,K)+1): # 同じ
        z = N-x-y 
        if 0 <= z <= K:
            count += 1

print(count)

# 解説
"""
コードの通り実装する(X,Y,Zの組み合わせ全て調べる)とO(N^3)になる
ここで X+Y+Z=N に注目する
Z = N-X-Yとすると Nが決まっているので、XとYがきまればZは自動的に決まることになる
あとはそのZが [0,K]内にあるかどうかだけ確認すれば良い
調べるのはXとYについてのみなのでこれはO(N^2)となる
"""