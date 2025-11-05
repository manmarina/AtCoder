K = int(input())
S = input()
T = input()

ls = len(S)
lt = len(T)

# 1文字挿入するケース
if ls == lt - 1:
    flag = False
    for i in range(lt):
        if i < ls and not flag:
            if S[i] != T[i]:  # 一致しなかったらフラグをたてて1文字見逃す
                flag = True
        else:
            if i == ls:  # 最後まで一致したら、最後に1文字挿入して一致
                break
            elif S[i - 1] != T[i]:  # フラグを立てた後、一致しなかったら
                print("No")
                exit()

# 1文字削除するケース
elif ls - 1 == lt:
    flag = False
    for i in range(ls):
        if i < lt and not flag:
            if S[i] != T[i]:  # 一致しなかったらフラグをたてて1文字見逃す
                flag = True
        else:
            if i == lt:  # 最後まで一致したら、最後を1文字削除して一致
                break
            if S[i] != T[i - 1]:  # フラグを立てた後、一致しなかったら
                print("No")
                exit()

# 1文字変換するケース
elif ls == lt:
    flag = False
    for i in range(ls):
        if not flag:
            if S[i] != T[i]:  # 一致しなかったらフラグをたてて1文字見逃す
                flag = True
        else:
            if S[i] != T[i]:  # フラグを立てた後、一致しなかったら
                print("No")
                exit()

# あてはまらないとき
else:
    print("No")
    exit()

# 全てクリアしたとき
print("Yes")

"""
場合分け系
1文字挿入するケース、1文字削除するケース、1文字変換するケースにわけて考える。

https://atcoder.jp/contests/abc386/tasks/abc386_c
"""
