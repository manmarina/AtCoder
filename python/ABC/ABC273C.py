from collections import Counter, defaultdict


N = int(input())
A = list(map(int, input().split()))

# カウンターを作成 Ai -> 個数
cnt = Counter(A)
# print(cnt)

# カウンターのキーを降順でソートして一旦リストに(先頭から0種類の個数、1種類の個数,2種類の個数...となる。)
cnt = sorted(cnt.items(), reverse=True)
# print(cnt)

# カウンターのキーの名前を0,1,2...に変更して辞書として再作成
cnt = {i: value for i, (_, value) in enumerate(cnt)}
# print(cnt)

# 辞書をdefaultdictに変更
dd = defaultdict(int, cnt)
# print(dd)

# 0から順に出力
for i in range(N):
    print(dd[i])

"""
問題文の理解が難解系
リトライ

1回目より早く何を出力すればよいか理解できた。
ロジックは前回と似ているが、辞書のキーを直接変更した点が異なる。
辞書のキーの操作について追加でチャッピーに質問した。
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6912178c-1098-8323-95f7-603be12b1f31

https://atcoder.jp/contests/abc273/tasks/abc273_c
https://chatgpt.com/c/68f9cb31-6254-8322-a131-341c7bdff8b7
"""
