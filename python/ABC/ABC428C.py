Q = int(input())

out = set()  # 不正な')'の出現位置を記録する変数

stack = []  # '(',')'を格納するスタック
score = 0  # '('は+1、')'は-1する。score==0が"Yes"の必要条件
for _ in range(Q):
    q = input().split()
    num = int(q[0])
    if num == 1:
        stack.append(q[1])

        # 不正な')'が出現したら位置をoutに格納
        if score == 0 and q[1] == ')':
            out.add(len(stack))

        if q[1] == '(':
            score += 1  # '('を追加したときのスコア調整
        else:
            score -= 1  # ')'を追加したときのスコア調整

    else:  # num == 2
        if len(stack) in out:  # 不正')'が存在する位置まで戻ってきたらoutから削除
            out.remove(len(stack))
        if stack.pop() == '(':
            score -= 1  # '('を削除したときのスコア調整
        else:
            score += 1  # ')'を削除したときのスコア調整

    if out:  # 不正な’)'が存在する限り"No"
        print("No")
    elif not stack:
        print("Yes")
    elif stack[0] != ')' and score == 0:
        print("Yes")
    else:
        print("No")

    # print(stack, score, out)

"""
自力解
コンテスト中は惜しくもWAだったが、
チャッピーにWAの原因を確認して調整したコードでAC
https://atcoder.jp/contests/abc428/tasks/abc428_c

鉄則本のp.297 B51もヒントになった。

チャッピーの意見を聞いて作成したオリジナル入力例
6
1 (
1 )
1 )
1 (
2
2

"""
