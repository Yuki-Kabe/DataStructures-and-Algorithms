# 年齢当てゲームの実装

print("Start Game!")

# Aさんの数の候補を表す区間を [left, right)と表す
left = 20
right = 36

# Aさんの数を 1つに絞れないうちは繰り返す
while right - left > 1:
    mid = left + (right - left)//2 # 区間の真ん中

    # mid 以上かを聞いて 回答を yes か no で受け取る
    ans = input("{} 歳未満ですか? (yes/no)".format(mid))

    if ans == "yes":
        right = mid
    elif ans == "no":
        left = mid

print("The age is {} !!".format(left))