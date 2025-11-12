N = int(input())
A = list(map(int, input().split()))

cnt4 = sum(a % 4 == 0 for a in A)  # 4の倍数の個数
cnt2 = sum(a % 2 == 0 and a % 4 != 0 for a in A)  # 2の倍数だが、4の倍数でない数の個数
cnt1 = N - cnt4 - cnt2  # 奇数の個数

if cnt2 == 0:  # 2の倍数だが、4の倍数出ない数が存在しない時
    print("Yes" if cnt4 >= cnt1 - 1 else "No")  # 4の倍数は、奇数に挟まれる文だけあれば良い
else:
    print("Yes" if cnt4 >= cnt1 else "No")  # 2の倍数だが、4の倍数でない数は、まとめて奇数一つと同じ働きをする

"""
数学的な気づき系
4の倍数でない2の倍数は、かけ合わせれば4の倍数になる。
4の倍数をすべてくっつけてならべてしまえば、それらの塊をまとめてひとつの奇数と同じ働きをする。
ということに気づくと答えが見えてくる。
チャッピーに説明してもらって理解できた。

けんちょん+チャッピー
https://drken1215.hatenablog.com/entry/2025/01/03/150449

https://atcoder.jp/contests/abc069/tasks/arc080_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6913f3cf-4cc4-8324-a13b-a8f64bd847ce
"""
