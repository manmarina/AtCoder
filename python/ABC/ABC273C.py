# 入力
n = int(input())
a_list = list(map(int, input().split()))

# map<int,int> mp と同様に辞書でカウント
mp = {}
for a in a_list:
    mp[a] = mp.get(a, 0) + 1
# print(mp)

# 降順で出力
for key in sorted(mp.keys(), reverse=True):
    print(mp[key])  # Aiより大きいものが0種類のものの個数から順に出力される

# 残りを 0 で埋める
for _ in range(n - len(mp)):
    print(0)


"""
問題文の理解が難解系

問題文を読んでも何を出力すればよいのかわかりづらい。
解説放送でも理解できなかった。
参考になったサイト
https://programming-hiroba.com/abc273-c/

出力は
K=0から始まり、K=N-1まで
(K = 0,1,2,...,N-1)

Aiより大きいものがちょうどK"種類"になるAiの"個数"を出力する

つまり、
2 7 1 8 2 8
の場合は、
8: 2個 -> 8より大きいものは0種類（0行目） -> 2個と出力
7: 1個 -> 7より大きいものは1種類（1行目） -> 1個と出力
2: 2個 -> 2より大きいものは2種類（2行目） -> 3個と出力
1: 1個 -> 1より大きいものは3種類（3行目） -> 4個と出力
4種類は0個
5種類は0個
6種類は0個
という出力になる。

https://atcoder.jp/contests/abc273/tasks/abc273_c
https://chatgpt.com/c/68f9cb31-6254-8322-a131-341c7bdff8b7
"""
