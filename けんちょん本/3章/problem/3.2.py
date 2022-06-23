N = int(input())
v = int(input())

List = list(map(int, input().split()))

count = 0
for i in List:
    if i == v:
        count += 1

print(count)
