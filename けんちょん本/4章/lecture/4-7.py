# フィボナッチ数列をfor文による反復で求める

F = [0 for _ in range(50)]
F[1] = 1

for i in range(2,50):
    F[i] = F[i-1] + F[i-2]
    print("{} 項目 : {}".format(i, F[i]))


