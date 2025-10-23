N = int(input())
A = list(map(int, input().split()))

ans = [A]  # 対戦結果を保持するリスト
# print(ans)

for i in range(N):  # トーナメントの階層
    temp = []
    for j in range(0, len(ans[i]), 2):  # 前回対戦結果から対戦ペアを決定
        l = ans[i][j]
        r = ans[i][j + 1]
        temp.append(max(l, r))  # レートの高いほうが勝ち
    ans.append(temp)  # この階層の対戦結果をリストに追加

# print(ans[-2][0])
print(A.index(min(ans[-2])) + 1)  # 決勝戦のレートの低い方のインデックス+1を表示

"""
シミュレーション系

トーナメントをそのままシミュレートします。
問題文のトーナメントの正確な定義に従って処理をします。

https://atcoder.jp/contests/abc188/tasks/abc188_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68fa00fc-ad2c-8324-af5a-c4f6e825d110
"""
