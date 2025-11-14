L, R = map(int, input().split())

# R - L >= 2019 の場合は必ず 0 が作れる
if R - L >= 2019:
    print(0)
else:  # そうでないときは、L,Rの範囲を全探索
    res = 2018
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            res = min(res, (i * j) % 2019)
    print(res)

"""
工夫して探索の通り数を減らす全探索 + 数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2019/07/07/233700
「2019 個以上連続した整数には 2019 の倍数が必ずある」ことに気づく。
もし R - L < 2019 なら
→ 区間の長さは高々 2019 個
→ この範囲なら、二重ループ全探索しても OK
（2019^2 ≒ 4,000,000 なので余裕で間に合う

https://atcoder.jp/contests/abc133/tasks/abc133_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6916a2bd-93ac-8321-a844-5cffa6716a9e
"""
