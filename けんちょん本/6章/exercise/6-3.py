import bisect

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.append(0)
P = [i + j for i in P for j in P]
P.sort()

ans = 0
for p in P:
    if M - p < 0:
        continue
    
    idx = bisect.bisect_right(P, M - p)
    ans = max(ans, p + P[idx - 1])

print(ans)


# Problem: https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# Submit: https://atcoder.jp/contests/joi2008ho/submissions/41065517
# Keyword: 半分全列挙